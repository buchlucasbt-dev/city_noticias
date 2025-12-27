//js searc
//alert("ikwjejj");


function loadSECev() {
	//alert("ola mundo");
	
	
	const dadoPesq = document.getElementById("inPesqEv").value;
	
	
	fetch("/loadsearchcmcev",{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      dadopesq: dadoPesq
    })
  })
  .then(response => response.json())
  .then(data => {
    //const btnClose = document.getElementById("btnDismissDel");
    //btnClose.innerHTML = "Fechar"; // muda texto do botão
    //alert(data[0]);
    
    
    
    if (data[0] == "") {
    	document.getElementById("mainBCardEv").innerHTML = "Nenhum Evento Encotrado!";	
    
    }else{
    	document.getElementById("mainBCardEv").innerHTML = data[0] 
    
    }
    
    
    
    
    //alert("ola mumdo ¹223");
    // aqui garantimos que o popup continua funcional
  })
  .catch(error => console.error('Erro:', error));
}


function loadSECcm() {
	//alert("ola mundo");
	
	
	const dadoPesq = document.getElementById("inPesqCm").value;
	
	
	fetch("/loadsearchcmccm",{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      dadopesq: dadoPesq
    })
  })
  .then(response => response.json())
  .then(data => {
    //const btnClose = document.getElementById("btnDismissDel");
    //btnClose.innerHTML = "Fechar"; // muda texto do botão
    //alert(data[0]);
    
    
    
    
    
    
    if (data[0] == ""){
    	document.getElementById("mainBCardCm").innerHTML = "Nenhum Comunicado Encotrado";
    }else{
    
    document.getElementById("mainBCardCm").innerHTML = data[0];
    
    }
    
    //alert("ola mumdo ¹223");
    // aqui garantimos que o popup continua funcional
  })
  .catch(error => console.error('Erro:', error));
}

//alert("ola bbb");
	


document.addEventListener("DOMContentLoaded", () => {
  //alert("Carregando DOM...");
  document.getElementById("btnSearchEv").addEventListener("click", loadSECev);
  //alert("Evento adicionado com sucesso!");
});
//77



document.getElementById("btnSearchCm").addEventListener("click", loadSECcm);
//99


