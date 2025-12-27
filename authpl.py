import time
import requests as req

API_KEY = "AIzaSyDCRgnRYaikOkhN5bzB_30nq0ivnDjzZ0g" #api key web aplication

EMAIL = "admin@citynoticias.bsoft"
PASSWORD = "CityNOTI1023cias!##"

_token_cache = {
    "idToken": None,
    "exp": 0
}


def get_id_token():
    # reutiliza se ainda for válido
    if _token_cache["idToken"] and time.time() < _token_cache["exp"]:
        return _token_cache["idToken"]

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

    payload = {
        "email": EMAIL,
        "password": PASSWORD,
        "returnSecureToken": True
    }

    r = req.post(url, json=payload)
    data = r.json()

    if "idToken" not in data:
        raise Exception(f"Erro Firebase Auth: {data}")

    _token_cache["idToken"] = data["idToken"]
    _token_cache["exp"] = time.time() + int(data["expiresIn"]) - 60

    return _token_cache["idToken"]
