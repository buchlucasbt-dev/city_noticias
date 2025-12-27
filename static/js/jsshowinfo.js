
//alert("js ligado")
//funcao para mostrar o conteudo


scEventos = document.getElementById("sc--eventos");
        scCommunic = document.getElementById("sc--communic");
        
        headInfo= document.getElementById("head-ev");
        headInfoCM= document.getElementById("head-cm");


        function showEvent() {
            //alert('mostrando os enventos');

            scEventos.style.display = 'block';
            headInfo.style.top = "-60px";
        }

        function dismissEvent() {
            scEventos.style.display = 'none';
            headInfo.style.top = "0px";
    

        }

        function showCommunic() {
            //alert('mostrando os enventos');

            scCommunic.style.display = 'block';
            headInfoCM.style.top = "-60px";
        }

        function dismissCommunic() {
            scCommunic.style.display = 'none';
            headInfoCM.style.top = "0px";
        }


//alert("fim das funcoes");





// Seleciona tanto os cards de eventos quanto de comunicados
const btnsShowEvCm = document.querySelectorAll(".box--card, .box--comunic");

// Adiciona evento de clique em cada card
btnsShowEvCm.forEach(card => {
  card.addEventListener("click", cfmShowInfo);
});

function cfmShowInfo(event) {
  // Garantir que pegamos o card principal, mesmo se clicar dentro (em img, h3, etc.)
  const card = event.currentTarget;

  // ID do card — precisa seguir o formato padronizado (ex: card_ev_1 ou card_cm_5)
  const idCompleto =  String(card.id);
  const idParts = idCompleto.split("_");
  
  let typeCard = "Desconhecido";

  if (idParts.includes("cm")) {
    typeCard = "Comunicado";
    
    imgCm = document.getElementById("sc--img--cm");
    
    titleCm = document.getElementById("sc--title--cm");
    
    
    
    
    contentCm = document.getElementById("sc--content--cm");
    
    
    
    cardContentCm = document.getElementById(idCompleto);
    
    
    
    tituloCardCm = cardContentCm.querySelector(".comunic--content .cmc--title h3").innerText;
    
    
    detalhesCardCm  = cardContentCm.querySelector(".comunic--content p").innerText;
    
    imgCardCm  = cardContentCm.querySelector(".comunic--head img").getAttribute("src");
    
    
    
    if (titleCm){
    
    	//alert("ola");
    	titleCm.innerText = tituloCardCm;
    	titleCm.style.color = "#000";
    	
    }
    contentCm.innerText = detalhesCardCm;
    contentCm.style.color = "#333";
    
    imgCm.src = imgCardCm;
    
    
    
    
    
    showCommunic()
    
    
  } else if (idParts.includes("ev")) {
    typeCard = "Evento";
    
    imgEv = document.getElementById("sc--img--ev");
    
    titleEv = document.getElementById("sc--title--ev");
    
    
    
    
    contentEv = document.getElementById("sc--content--ev");
    
    
    
    cardContent = document.getElementById(idCompleto);
    
    tituloCard = cardContent.querySelector("h3").innerText;
    
    
    detalhesCard = cardContent.querySelector("p").innerText;
    
    imgCard = cardContent.querySelector("img").getAttribute("src");
    
    
    titleEv.innerText = tituloCard;
    
    contentEv.innerText = detalhesCard;
    imgEv.src = imgCard;
    
    
    
    
    showEvent()
    
    
    
  }

  //alert(`O card é de um ${typeCard}`);
}


//and funcao mostrar eventos e comunicados