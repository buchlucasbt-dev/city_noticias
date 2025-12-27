
const boxEv = document.getElementById('sc_event_cmc');

const boxComu = document.getElementById('sc_comunic_cmc');

const boxCommit_ev = document.getElementById('sc_commit_eve');

const boxCommit_cm = document.getElementById('sc_commit_comu');

const mDash = document.getElementById('m-dash');

const boxMsg = document.getElementById("sc_msg_cmc");



    


function showCommitEve(){

	boxCommit_ev.style.display = "block";
	boxComu.style.display = "none";
	
	 boxCommit_cm.style.display = "none";
	 
	 boxEv.style.display = "none";
	 mDash.style.display = "none";
	 boxMsg.style.display = "none";
}


function showCommitComu() {
    boxCommit_cm.style.display = "block";
    boxCommit_ev.style.display = "none";
    
    boxComu.style.display = "none";
    
    boxEv.style.display = "none";
    mDash.style.display = "none";
    boxMsg.style.display = "none";
}

function showEve(){

	boxEv.style.display = "block";
	boxCommit_ev.style.display = "none";
	
	boxComu.style.display = "none";
	boxCommit_cm.style.display = "none";
	mDash.style.display = "none";
	boxMsg.style.display = "none";
	
}


function showComu() {
    boxComu.style.display = "block";
    boxCommit_ev.style.display = "none";
    
    boxCommit_cm.style.display = "none";
    
    boxEv.style.display = "none";
    mDash.style.display = "none";
    boxMsg.style.display = "none";
    
}


function showDash() {
    boxComu.style.display = "none";
    boxCommit_ev.style.display = "none";
    
    boxCommit_cm.style.display = "none";
    
    boxEv.style.display = "none";
    mDash.style.display = "block";
    boxMsg.style.display = "none";
    
}

function showMsg() {
    boxComu.style.display = "none";
    boxCommit_ev.style.display = "none";
    
    boxCommit_cm.style.display = "none";
    
    boxEv.style.display = "none";
    mDash.style.display = "none";
    
    boxMsg.style.display = "block";
    
    
    allMsgread()
    
}

function allMsgread(){
 
	
	
	
			formData = new FormData();
			
			formData.append("msg","mensagens lidas");
			
			
			
			fetch('/readed_cmcmsg', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data[0]);
                //bodyNotas.innerHTML = "";
                //bodyNotas.innerHTML = data[1]
                
                
            })
            .catch(error => console.error('Erro:', error));
        	
}



function loadCommitEv2(){
	alert("ola como esta");
}
function loadCommitEv(event){
			event.preventDefault();
			
			const tituloEv = document.getElementById('inEvTitulo').value;
			
			const dataEv = document.getElementById('inEvData').value;
			
			const detalheEv = document.getElementById('inEvDetalhe').value;
			const checkBtnEv = document.getElementById('check--feito--cmc--ev').value;
			
			
			const imageEv = document.getElementById('inEvImage');
			
			formData = new FormData();
			
			formData.append("tituloev", tituloEv);
			formData.append("dataev", dataEv);
			formData.append("detalheev", detalheEv);
			
			formData.append("checkbtnev",  checkBtnEv);
			formData.append("imageev",imageEv.files[0]);
			
			
			
			fetch('/commitEvent_cmc', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data[0]);
                //bodyNotas.innerHTML = "";
                //bodyNotas.innerHTML = data[1]
                
                
            })
            .catch(error => console.error('Erro:', error));
        	
        	
        	
        	
        	
        	
        }


function loadCommitComu(event){
    event.preventDefault();

    const tituloCm = document.getElementById('inCmTitulo').value;
    const dataCm = document.getElementById('inCmData').value;
    const detalheCm = document.getElementById('inCmDetalhe').value;
    const checkBtnCm = document.getElementById('check--feito--cmc--cm').value;
    const imageCm = document.getElementById('inCmImage');

    const formData = new FormData();
    formData.append("titulocm", tituloCm);
    formData.append("datacm", dataCm);
    formData.append("detalhecm", detalheCm);
    formData.append("checkbtncm", checkBtnCm)

    if (imageCm.files.length > 0) {
        formData.append("imagecm", imageCm.files[0]);
    }

    fetch('/commitComunic_cmc', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Erro no envio: " + response.status);
        }
        return response.json();
    })
    .then(data => {
        alert(data[0]);
        // Atualizar DOM se necessário
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Erro ao enviar dados: " + error.message);
    });
}


// área para apagar eventos e comunicados
const btnsDl = document.querySelectorAll(".btn_dh_dl");

btnsDl.forEach(btndl => {
  btndl.addEventListener("click", cfmDelete);
});

function cfmDelete(event) {
  const btnClickDel = event.target;
  const fg = String(btnClickDel.id).split("_");
  
  let typeInfo; // <-- aqui o let é necessário
  
  if (fg[1] == "cm") {
    typeInfo = "Comunicado";
  } else {
    typeInfo = "Evento";
  }
 
}



function cfmDelete(event) {
  const btnClickDel = event.target;
  const fg = String(btnClickDel.id).split("_");
  
  let typeInfo;

  if (fg[1] === "cm") {
    typeInfo = "Comunicado";
  } else {
    typeInfo = "Evento";
  }

  // Atualiza o conteúdo do popup
  document.getElementById("popnumInfo").innerHTML = fg[0];
  document.getElementById("nomedltext").innerHTML = typeInfo;
  document.getElementById("poptypeInfo").innerHTML = typeInfo;

  // Exibe o popup
  document.getElementById("main-p-dl").style.display = "flex";
}

function dismissPopDell(){
	//alert("olaumdo");
	document.getElementById("main-p-dl").style.display = "none";
	
	//document.getElementById("btndlcfm").style.display = "block";
	
	
	
	
}


function cfmDellInfo(){
  const numIdInfo = document.getElementById("popnumInfo").textContent;
  const typeInfoText = document.getElementById("nomedltext").textContent;
  
  fetch("/dellinfo",{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      typeinfocmc: typeInfoText,
      numeroinfocmc: numIdInfo
    })
  })
  .then(response => response.json())
  .then(data => {
    const btnClose = document.getElementById("btnDismissDel");
    btnClose.innerHTML = "Fechar"; // muda texto do botão
    
    
    const btnCFM = document.getElementById("btndlcfm");
    
    btnCFM.style.visibility = "hidden";
    
    document.getElementById("titlepopdel").innerText = 
      data[0] === "sim" ? "Eliminado!" : "Falha na Eliminação!";
    
    document.getElementById("maintextpopinfodell").innerHTML = 
      data[0] === "sim"
      ? `O ${data[1]} foi eliminado com sucesso.`
      : `Não foi possível eliminar o ${data[1]}. Tente mais tarde!`;

    // aqui garantimos que o popup continua funcional
  })
  .catch(error => console.error('Erro:', error));
}




// Função para fechar e resetar o popup

function closePopDel() {
  const mainPop = document.getElementById("main-p-dl");
  
  mainPop.style.display = "none"; // esconde o popup
  document.getElementById("btnDismissDel").innerHTML = "Cancelar"; // restaura o texto original do botão
  
  const btnCFM = document.getElementById("btndlcfm");
    
    btnCFM.style.visibility = "visible";
  
  
  document.getElementById("titlepopdel").innerText = "Pedindo Confirmação";
  document.getElementById("maintextpopinfodell").innerHTML = 
    'Pretende eliminar este <b id="nomedltext"></b>?';
  document.getElementById("popnumInfo").innerText = "";
  document.getElementById("poptypeInfo").innerText = "";
}


  
  //alert("Tem certeza que pretende eliminar este: " + typeInfo);
 
 
// área para apagar mensagens dos municipes


const btnsDlMsg = document.querySelectorAll(".delete-btn-msg");

btnsDlMsg.forEach(btndlmsg => {
  btndlmsg.addEventListener("click", cfmDeleteMsg);
});

function cfmDeleteMsg(event) {
  const btnClickDelMsg = event.target;
  const fgmsg = String(btnClickDelMsg.id).split("_");
  
  let typeInfoMsg; // <-- aqui o let é necessário
  
  if (fgmsg[1] == "msg") {
    typeInfoMsg = "Mensagem";
  } else {
    typeInfoMsg = "Mensagem2";
  }
  
  //alert("Tem certeza que pretende eliminar este: " + typeInfo);
 
  document.getElementById("popnumInfoMsg").innerHTML = fgmsg[0];
  
  document.getElementById("nomedltextmsg").innerHTML = typeInfoMsg;
  document.getElementById("poptypeInfoMsg").innerHTML = typeInfoMsg;
  document.getElementById("main-p-dl-msg").style.display = "flex";
  
  
}

function dismissPopDellMsg(){
	//alert("olaumdo");
	document.getElementById("main-p-dl-msg").style.display = "none";
	
	//document.getElementById("btndlcfm").style.display = "block";
	
	
	
	
}

function cfmDellInfoMsg(){
  const numIdInfoMsg = document.getElementById("popnumInfoMsg").textContent;
  const typeInfoTextMsg = document.getElementById("nomedltextmsg").textContent;
  
  fetch("/dellinfomsg",{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      typeinfocmcmsg: typeInfoTextMsg,
      numeroinfocmcmsg: numIdInfoMsg
    })
  })
  .then(response => response.json())
  .then(data => {
    const btnCloseMsg = document.getElementById("btnDismissDelMsg");
    btnCloseMsg.innerHTML = "Fechar"; // muda texto do botão
    const btnCFMMsg = document.getElementById("btndlcfmmsg");
    
    
    btnCFMMsg.style.visibility = "hidden";
    
    
    let btnDlCard;
    
    
    numIdBtn = document.getElementById("popnumInfoMsg").textContent;
    
    btnDlCard = numIdBtn+"_msg"
    
    if (data[0] == "sim") {
    	document.getElementById(btnDlCard).innerText = "Eliminado";
    	
    	
    
    
    }
    //alert(btnDlCard);
    
    
    document.getElementById("titlepopdelmsg").innerText = 
      data[0] === "sim" ? "Eliminado!" : "Falha na Eliminação!";
    
    document.getElementById("maintextpopinfodellmsg").innerHTML = 
      data[0] === "sim"
      ? `A ${data[1]} foi eliminada com sucesso.`
      : `Não foi possível eliminar a ${data[1]}. Tente mais tarde!`;

    // aqui garantimos que o popup continua funcional
  })
  .catch(error => console.error('Erro:', error));
}




// Função para fechar e resetar o popup

function closePopDelMsg() {
  const mainPopMsg = document.getElementById("main-p-dl-msg");
  
  mainPopMsg.style.display = "none"; // esconde o popup
  document.getElementById("btnDismissDelMsg").innerHTML = "Cancelar"; // restaura o texto original do botão
  
  
  const btnCFMMsg = document.getElementById("btndlcfmmsg");
    
  
    btnCFMMsg.style.visibility = "visible";
  
  
  
  
  document.getElementById("titlepopdelmsg").innerText = "Pedindo Confirmação";
  document.getElementById("maintextpopinfodellmsg").innerHTML = 
    'Pretende eliminar este <b id="nomedltextmsg"></b>?';
  document.getElementById("popnumInfoMsg").innerText = "";
  document.getElementById("poptypeInfoMsg").innerText = "";
}



// área para desabilitar e abilitar  a visibilidade dos eventos e comunicados

const btnsVsi = document.querySelectorAll(".btn_dh_vsi");

btnsVsi.forEach(btnvsi => {
  btnvsi.addEventListener("click", cfmVisivel);
});

function cfmVisivel(event) {
  const btnClickVsi= event.target;
  const fgvsi = String(btnClickVsi.id).split("_");
  
  const btnText = btnClickVsi.textContent.trim().toLowerCase();
  
  let typeInfoVsi; // usar let para nao difinir valor ao decrarar
  
  if (fgvsi[1] == "ev") {
    typeInfoVsi = "evento";
  } else {
    typeInfoVsi = "comunicado";
  }
  
  //alert("Tem certeza que pretende eliminar este: " + typeInfo);
 
  document.getElementById("popnumInfoVsi").innerHTML = fgvsi[0];
  
  
  //mudando o texto segundo a situacao
  
  let dataTextCard;
  
  if (btnText == "visivel"){
  	dataTextCard = `Pretende esconder o `;
  }else{
  	dataTextCard = `Pretende activar a visibilidade deste `;
  }
  
  document.getElementById("maintextpopinfovsi").innerHTML =  dataTextCard+"<b id='nomevsitext'></b>?";
  
  
  
  
  document.getElementById("nomevsitext").innerHTML = typeInfoVsi;
  document.getElementById("poptypeInfoVsi").innerHTML = typeInfoVsi;
  document.getElementById("main-p-vsi").style.display = "flex";
  
  //alert(btnText);
  
  
  
	    
	    
  
  
}

function dismissPopVsi(){
	//alert("olaumdo");
	document.getElementById("main-p-vsi").style.display = "none";
	
	//document.getElementById("btndlcfm").style.display = "block";
	
	
	
	
}

function cfmVsiInfo(){
  const numIdInfoVsi = document.getElementById("popnumInfoVsi").textContent;
  const typeInfoTextVsi = document.getElementById("nomevsitext").textContent;
  
  fetch("/atualizationinfovsi",{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      typeinfocmcvsi: typeInfoTextVsi,
      numeroinfocmcvsi: numIdInfoVsi
    })
  })
  .then(response => response.json())
  .then(data => {
    const btnCloseVsi = document.getElementById("btnDismissVsi");
    btnCloseVsi.innerHTML = "Fechar"; // muda texto do botão
    const btnCFMVsi = document.getElementById("btncfmvsi");
    
    
    
    
    btnCFMVsi.style.visibility = "hidden";
    
    
    //ola
    
    const popNIVsi = document.getElementById("popnumInfoVsi");
    
    numDoId = popNIVsi.textContent;
    
    
    if (data[1] == "comunicado"){
    	//alert("E um comunicado");
    	allId = numDoId+"_cm"
    	btnCardVsi = document.getElementById(allId);
    	
    	
    	btnCardVsi.innerHTML = data[2]
    	
    	
    
    
    }else{
    	allId = numDoId+"_ev"
    	
    	btnCardVsi = document.getElementById(allId);
    	
    	btnCardVsi.innerHTML = data[2]
    	
  }
    
    
    //and ola
    
    
    if (data[2] == "Visivel"){
	    
	    document.getElementById("titlepopvsi").innerText = 
	      data[0] === "sim" ? "Visibilidade Activa!" : "Falha na Visibilidade!";
	    
	    document.getElementById("maintextpopinfovsi").innerHTML = 
	      data[0] === "sim"
	      ? `O ${data[1]} foi tornado visivel novamente.`
	      : `Não foi possível activar a visibilidade do ${data[1]}. Tente mais tarde!`;
    }else{
    	
    	document.getElementById("titlepopvsi").innerText = 
	      data[0] === "sim" ? "Escondido com sucesso!" : "Falha ao Esconder!";
	    
	    document.getElementById("maintextpopinfovsi").innerHTML = 
	      data[0] === "sim"
	      ? `O ${data[1]} foi escondido do publico.`
	      : `Não foi possível esconder o ${data[1]}. Tente mais tarde!`;
    	
    }

    // aqui garantimos que o popup continua funcional
  })
  .catch(error => console.error('Erro:', error));
}




// Função para fechar e resetar o popup

function closePopVsi() {
  const mainPopVsi = document.getElementById("main-p-vsi");
  
  mainPopVsi.style.display = "none"; // esconde o popup
  document.getElementById("btnDismissVsi").innerHTML = "Cancelar"; // restaura o texto original do botão
  
  
  const btnCFMVsi = document.getElementById("btncfmvsi");
    
  
    btnCFMVsi.style.visibility = "visible";
  
 





  
  
  document.getElementById("titlepopvsi").innerText = "Pedindo Confirmação";
  document.getElementById("maintextpopinfovsi").innerHTML = 
    'Pretende esconder este <b id="nomevsitext"></b>?';
  document.getElementById("popnumInfoVsi").innerText = "";
  document.getElementById("poptypeInfoVsi").innerText = "";
}




//area para pesquisar eventos e comunicados



// liga o botão "Cancelar" / "Fechar" a esta função
document.getElementById("btncfmvsi").addEventListener("click", cfmVsiInfo);


document.getElementById("btnDismissVsi").addEventListener("click", dismissPopVsi);


document.getElementById("btnDismissVsi").addEventListener("click", closePopVsi);
//ola como esta

document.getElementById("btndlcfm").addEventListener("click", cfmDellInfo);


document.getElementById("btnDismissDel").addEventListener("click", dismissPopDell);


document.getElementById("btnDismissDel").addEventListener("click", closePopDel);
//ola como esta




document.getElementById("btndlcfmmsg").addEventListener("click", cfmDellInfoMsg);


document.getElementById("btnDismissDelMsg").addEventListener("click", dismissPopDellMsg);


document.getElementById("btnDismissDelMsg").addEventListener("click", closePopDelMsg);
//ola como esta



document.getElementById("loadCommitBtn").addEventListener("click", loadCommitComu);

document.getElementById("loadCommitBtnEv").addEventListener("click", loadCommitEv);


function updateInfoDash() {
  fetch('/updateinfodash', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ action: "update" }) // opcional
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Erro ao atualizar dashboard");
    }
    return response.json();
  })
  .then(data => {
    // validação básica
    if (!Array.isArray(data)) {
      console.error("Resposta inválida:", data);
      return;
    }

    // atualiza os números no dashboard
    const nMsgT = document.getElementById("nM");
    const nMsgNovo = document.getElementById("nMN");
    
    
    const numCT= document.getElementById("nC");
    const numEvT = document.getElementById("nEv");
    
    

    numEvT.innerText = data[0] ?? 0;
    numCT.innerText = data[1] ?? 0;
    nMsgT.innerText = data[2] ?? 0;
    nMsgNovo.innerText = (data[3] ?? 0) + " mensagens novas";

  })
  .catch(error => {
    console.error("Erro updateInfoDash:", error);
  });
}


function atualizarDash() {
  updateInfoDash()
}

setInterval(atualizarDash, 20000); // a cada 20s



