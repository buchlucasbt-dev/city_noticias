from flask import Flask,render_template,url_for,request,jsonify,redirect,session

from functools import wraps





import requests as req
import json

import cloudinary
import cloudinary.uploader

from datetime import datetime, date , timedelta


#importando auteticacao do servidor
from authpl import get_id_token



#Senha E Nome do Usuario

passwordcn = "n5601" #senha do Administrador
usercn = "Buch" # nome do administrador

#----------------------#



# Configurar Cloudinary com suas credenciais
cloudinary.config(
    cloud_name='dhfytj5nq',
    api_key='144515411569918',
    api_secret='qvlOr_FAX61h61GzlkMig9W2p6w'
)




	




firebaseURL = "https://portal-cmchimoio-default-rtdb.firebaseio.com"

def loadDashCMC():
	
	
	token = get_id_token()
	
	
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	
	
	rotaEv = "Eventos"
	rotaCm = "Comunicados"
	rotaMsg = "Mensagens"
	
	resEv = resInfoCm.get(rotaEv, {})
	resCm = resInfoCm.get(rotaCm, {})
	resMsg = resInfoCm.get(rotaMsg, {})
	
	
	
	
	lengthEv = str(len(resEv))
	lengthCm = str(len(resCm))
	
	lengthMsg = str(len(resMsg))
	
	
	
	
	
	
	allDataLen = [lengthEv,lengthCm,lengthMsg]
	
	
	#startar listagem d3 ids
	
	
	
	#armazenar ids na lista para analizar
	listIdsMsg = []
	publiVisiveis = 0
	publiInvisiveis = 0
	
	
	for cMsg in resMsg:
		msgCMC = resMsg[cMsg]
		
		numIdMsg = msgCMC['numero']
		
		
		if numIdMsg.isnumeric():
			
			
			
			listIdsMsg.append(numIdMsg)
	
	listIdsEvs = []
	
	
	for cEv in resEv:
		
		eventC = resEv[cEv]
		
		numIdEv = eventC['numero']
		
		if "visi" in eventC:
			resv = eventC["visi"]
			
			if resv == "on":
				publiVisiveis = publiVisiveis + 1
			else:
				publiInvisiveis = publiInvisiveis +1
			
		else:
			
			publiVisiveis = publiVisiveis + 1
			
	
		
		
		if numIdEv.isnumeric():
			
			listIdsEvs.append(numIdEv)
			
			
	
	listIdsCm = []
	
	
	for cCm in resCm:
		
		comuC = resCm[cCm]
		
		numIdCm = comuC['numero']
		
		
		if "visi" in comuC:
			resv2 = comuC["visi"]
			
			if resv2 == "on":
				publiVisiveis = publiVisiveis + 1
			else:
				publiInvisiveis = publiInvisiveis +1
			
		else:
			
			publiVisiveis = publiVisiveis + 1
		
		
		if numIdCm.isnumeric():
			
			listIdsCm.append(numIdCm)
			
	
	
	
	
	#load comunicados
	
	listIdsCm = sorted(listIdsCm, reverse = True)
	
	listIdsEvs = sorted(listIdsEvs, reverse = True)
	
	listIdsMsg = sorted(listIdsMsg, reverse = True)
	
	
	#print(listIdsCm)
	#print(listIdsEvs)
	#print(listIdsMsg)
	
	
	#and starter listagem de ids 
	
	allDataMsg = ""
	numNewMsg = 0
	for cIdMsg in listIdsMsg:
		
		for cMsg in resMsg:
			#print(cMsg)
			
			msg = resMsg[cMsg]
			
			numM = msg['numero']
			
			
			
			if str(cIdMsg) == str(numM):
				idCardMsg = numM+"_msg"
				#print("numero id msg:", numM)
				
				dataM = msg["data"]
				nomeM = msg["nome"]
				msgD = msg["msg"]
				numTell = msg["tell"]
				emailM = msg["email"]
				
				emailH = msg["hora"]
				
				if "nova" in msg:
					
					novaM = msg["nova"]
					
					if novaM == "1":
						numNewMsg = numNewMsg +1
					else:
						...
				else:
					novaM = "0"
				
				allDataMsg = allDataMsg + f""" <div class="msg-box">
               	<h3>{nomeM}</h3>
               	<div>
               	<h4>Tell: {numTell}</h4>
               	<h4>Emal: {emailM}</h4>
               	<small>ID da Mensagem: {numM}</small>
               	<hr>
               	<p>{msgD}</a>
               	
               	</div>
               	<small>hora: {emailH}</small><small> | data: {dataM}</small><button class="delete-btn-msg" id="{idCardMsg}">Eliminar</buttin>
               
               
               </div>
               
              
"""
				
				
	
	#load comunicados
	
	allDataComunic = ""
	for cIdCm in listIdsCm:
		
		
		
		for cComu in resCm:
			
			
			
			#print(cComu)
			
			comunicado = resCm[cComu]
			
			numC  = comunicado["numero"]
			
			if str(cIdCm) == str(numC):
				#print("numro dash", numC)
				
				tituloC = comunicado['titulo']
				
				detalhes = comunicado["detalhes"]
				
				linkImg = comunicado["linkimg"]
				
				dataCm = comunicado["data"]
				
				
				idBtnVSI = str(numC)+ "_cm"
				
				imgComunic = linkImg
				
				idCardBtn = str(numC)+"_cm"
				if "visi" in comunicado:
					resvisi = comunicado["visi"]
					
					if resvisi == "on":
						statusVisi = "Visivel"
					else:
						statusVisi = "Invisivel"
				else:
					statusVisi  = "Visivel"
				
				
				
				allDataComunic = allDataComunic +f"""
				
				
		                <div onclick="showCommunic()" class="box--comunic">
		                    <div class="comunic--head">
		
		                        <img src="{linkImg}" alt="imgcominic" />
		                        
		                    </div>
		                    <div class="comunic--content">
		                        <div class="cmnc--title">
		
		                            <h2>{tituloC}</h2>
		                            <small>📅 Data: {dataCm}</small>
		                            <small>🔢 Comunicado N°: {numC}</small>
		                        </div>
		                        <div class="cmnc--title">
		                            <p>{detalhes}</p>
		                        </div>
		                        
		                        <button class="btn_dh_vsi" id="{idBtnVSI}">{statusVisi}</button>
		                        <button id="{idCardBtn}" class="btn_dh_dl">Eliminar</button>
		                        
		
		
		                    </div>
		
		                </div>
				
				"""
		
	
	#load eventos
	allDataEvent = ""
	
	
	for cIdEv in listIdsEvs:
		
		
		
		
		for cEv in resEv:
			
			evento = resEv[cEv]
			
			numEv = evento['numero']
			
			if str(cIdEv) == str(numEv):
				#print("dash Evento ", numEv)
				
				detalhesEv = evento['detalhes']
				
				tituloEv = evento['titulo']
				dataEv = evento['data']
				linkImgEv = evento["linkimg"]
				
				if "visi" in evento:
					resvisi = evento["visi"]
					if resvisi == "on":
						statusVisiEv ="Visivel"
					else:
						statusVisiEv = "Invisivel"
				else:
					statusVisiEv = "Visivel"
				
				
				idCardBtn = str(numEv)+ "_ev"
				idBtnVsi = str(numEv)+ "_ev"
				
				
				allDataEvent = allDataEvent +f"""<div onclick="showEvent()" class="box--card">
				<h3>{tituloEv}</h3>
				
				 <small>📅 Data: {dataEv} </small>
				 <small>🔢 Evento N°: {numEv}</small>
				
				<img src="{linkImgEv}" alt="patricio" />
		        <br>
		        <p  class="deta_dash">{detalhesEv}</p>
		        
		        <div>
		          <button class="btn_dh_vsi" id="{idBtnVsi}">{statusVisiEv}</button>
		                    <button id="{idCardBtn}" class="btn_dh_dl">Eliminar</button>
		        
		       
		        </div>
		        </div>
		        
		        
		        """
		
		
	
	
	dataStatus = [numNewMsg,publiVisiveis,publiInvisiveis]
	
	return [allDataComunic,str(allDataEvent),allDataMsg,allDataLen,dataStatus]


#Comunicados funcao dedicada


def loadComunic():
	
	token = get_id_token()
	
	
	
	
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	rotaCm = "Comunicados"
	
	resCm = resInfoCm[rotaCm]
	
	
	
	
	#armazenar ids na lista para analizar
	
	infoNewComunic = []
	
	
	listIdsCm = []
	
	
	for cCm in resCm:
		
		comuC = resCm[cCm]
		
		numIdCm = comuC['numero']
		
		
		if numIdCm.isnumeric():
			
			listIdsCm.append(numIdCm)
			
	
	
	
	
	#load comunicados
	
	listIdsCm = sorted(listIdsCm, reverse = True)
	
	
	
	print(listIdsCm)
	
	
	countCm = 0
	allDataFCAC = ""
	allDataComunic = ""
	for numE in listIdsCm:
		
		
		
		
		
		
		
		for cComu in resCm:
			
			
			comunicado = resCm[cComu]
			numComu = comunicado['numero']
			
			
			
			
			
			if str(numE) == str(numComu):
				
				print("numero encotrado")
				
				
				tituloC = comunicado['titulo']
				
				detalhes = comunicado["detalhes"]
				
				linkImg = comunicado["linkimg"]
				
				numC  = comunicado["numero"]
				
				dataCm = comunicado["data"]
				
				if "visi" in comunicado:
					resvisiC = comunicado['visi']
					if resvisiC == "on":
						statusV = "visiv12"
					else:
						statusV = "invisi12"
				else:
					statusV = "visiv12"
				
				
				
				if statusV != "visiv12":
					...
				else:
						
					if str(numComu) == listIdsCm[0]:
						
						infoNewComunic.append(tituloC)
						infoNewComunic.append(numC)
						infoNewComunic.append(dataCm)
						infoNewComunic.append(linkImg)
						infoNewComunic.append(detalhes)
						
						
						
					
					if "fcac" in comunicado:
						checkFCAC = comunicado["fcac"]
					else:
						checkFCAC = "off"
					
					imgComunic = linkImg
					
					
					countCm = countCm +1
					idCardCm = str(numC)+"_cm_card"
					
					if countCm <= 0:
						break
					else:
						
						if str(checkFCAC) == "on":
							
							allDataFCAC = allDataFCAC + f"""
							<div class=":box--feito"><img src="{imgComunic}"/>
							
	    <div id="box--feto--content">
	    
	    <p class="titulo-f">{detalhes}</p>
	    
	    </div
	    <p class="text--data--f">Data: {dataCm}</p>
	    </div> """
							print("Feito do Municipeo")
							
						
						allDataComunic = allDataComunic +f"""
						
						
				                <div  class="box--comunic" id="{idCardCm}">
				                    <div class="comunic--head">
				
				                        <img src="{imgComunic}" alt="imgcominic" />
				                        
				                    </div>
				                    <div class="comunic--content">
				                        <div class="cmc--title">
				
				                            <h3>{tituloC}</h3>
				                            <small>📅 Data: {dataCm}</small>
	<small>🔢 Comunicado N°: {numC}</small>
				                           
				                        </div>
				                        
				                            <p>{detalhes}</p>
				                       
				                        
				
				
				                    </div>
				
				                </div>
						
						"""
		
	
	
	
	
	return [allDataComunic,infoNewComunic]


#fim da funcao dedicada de comunicados

#funcao dedicada a Eventos

#Eventos e Comunicados para o Home
def loadEvent():
	token = get_id_token()
	
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	
	
	rotaEv = "Eventos"
	
	resEv = resInfoCm[rotaEv]
	
	
	
	
	#armazenar ids na lista para analizar
	
	infoNewEvent = []
	listIdsEvs = []
	
	
	for cEv in resEv:
		
		eventC = resEv[cEv]
		
		numIdEv = eventC['numero']
		
		
		if numIdEv.isnumeric():
			
			listIdsEvs.append(numIdEv)
			
			
	
	
	
	
	#load Eventos
	
	listIdsEvs = sorted(listIdsEvs, reverse = True)
	
	
	
	print(listIdsEvs)
	
	
	
	allDataFCAC = ""
	
	
	#load eventos
	allDataEvent = ""
	
	countEvs = 0
	for numEs in listIdsEvs:
		
		
		
		
		
		
		
		
		
		for cEve in resEv:
			
			evento = resEv[cEve]
			detalhesEv = evento['detalhes']
			
			numEvent = evento['numero']
			
			
			
			
			if str(numEs) == str(numEvent):
				
				print("numero encotrado 2")
						
				
				
				tituloEv = evento['titulo']
				
				numEv = evento['numero']
				
				dataPubli = evento['data']
				linkImgEv = evento["linkimg"]
				
				
				
				
				
				
				if "visi" in evento:
					resvisiEv = evento["visi"]
					
					if resvisiEv == "on" :
						statusVEv = "visiv7"
					else:
						statusVEv = "invisi7"
				else:
					statusVEv= "visiv7"
				
				if statusVEv != "visiv7":
					...
				
				
				
				
				
				else:
					
					
					if str(numEv) == listIdsEvs[0]:
						
						infoNewEvent.append(tituloEv)
						infoNewEvent.append(numEv)
						infoNewEvent.append(dataPubli)
						infoNewEvent.append(linkImgEv)
						infoNewEvent.append(detalhesEv)
						
						
					
					
					
					
					if "fcac" in evento:
						
						checkFCAC = evento["fcac"]
					else:
						checkFCAC = "off"
					
					countEvs = countEvs +1
					
					
					idCardEv = str(numEv)+"_ev_card"
					
					if countEvs <= 0:
						break
					else:
						
						if str(checkFCAC) == "on":
							allDataFCAC = allDataFCAC + f"""
							<div class="box--feito"><img src="{linkImgEv}"/>
							
	    <div id="box--feto--content">
	    
	    <p class="titulo-f">{detalhesEv}</p>
	    
	    </div
	    <p class="text--data--f">Data: {dataPubli}</p>
	    </div> """
							print("on no envento encotrado.")
						
						allDataEvent = allDataEvent +f"""<div class="box--card" id="{idCardEv}">
						
						<h3>{tituloEv}</h3>
						<small>📅 Data: {dataPubli}</small>
	<small>🔢 Evento N°: {numEv}</small>
						 
						 
						 
						 <img src="{linkImgEv}" alt="event image" />
						
						
				        <br>
				        <p>{detalhesEv}</p>
				        
				       
				        
				        </div>
				        
				        
				        """
		
		
	
	return [str(allDataEvent),infoNewEvent]


#and funcao dedicada a eventos





#Eventos e Comunicados para o Home
def loadComunicEvent():
	
	token = get_id_token()
	
	
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	
	
	rotaEv = "Eventos"
	rotaCm = "Comunicados"
	
	resEv = resInfoCm[rotaEv]
	resCm = resInfoCm[rotaCm]
	
	
	
	
	#armazenar ids na lista para analizar
	
	infoNewEvent = []
	listIdsEvs = []
	
	
	for cEv in resEv:
		
		eventC = resEv[cEv]
		
		numIdEv = eventC['numero']
		
		
		if numIdEv.isnumeric():
			
			listIdsEvs.append(numIdEv)
			
			
	
	listIdsCm = []
	
	
	for cCm in resCm:
		
		comuC = resCm[cCm]
		
		numIdCm = comuC['numero']
		
		
		if numIdCm.isnumeric():
			
			listIdsCm.append(numIdCm)
			
	
	
	
	
	#load comunicados
	
	listIdsCm = sorted(listIdsCm, reverse = True)
	
	listIdsEvs = sorted(listIdsEvs, reverse = True)
	
	
	print(listIdsCm)
	print(listIdsEvs)
	
	
	countCm = 0
	allDataFCAC = ""
	allDataComunic = ""
	for numE in listIdsCm:
		
		
		
		
		
		
		
		for cComu in resCm:
			
			
			comunicado = resCm[cComu]
			numComu = comunicado['numero']
			
			
			
			
			
			if str(numE) == str(numComu):
				
				print("numero encotrado")
				
				
				tituloC = comunicado['titulo']
				
				detalhes = comunicado["detalhes"]
				
				linkImg = comunicado["linkimg"]
				
				numC  = comunicado["numero"]
				
				dataCm = comunicado["data"]
				
				if "visi" in comunicado:
					resvisiC = comunicado['visi']
					if resvisiC == "on":
						statusV = "visiv12"
					else:
						statusV = "invisi12"
				else:
					statusV = "visiv12"
				
				
				
				if statusV != "visiv12":
					...
				else:
						
					if str(numComu) == listIdsCm[0]:
						
						infoNewEvent.append(tituloC)
						infoNewEvent.append(numC)
						infoNewEvent.append(dataCm)
						infoNewEvent.append(linkImg)
						infoNewEvent.append(detalhes)
						
						
						
					
					if "fcac" in comunicado:
						checkFCAC = comunicado["fcac"]
					else:
						checkFCAC = "off"
					
					imgComunic = linkImg
					
					
					countCm = countCm +1
					
					
					if countCm >= 4:
						break
					else:
						
						if str(checkFCAC) == "on":
							
							allDataFCAC = allDataFCAC + f"""
							<div class="box--feito">
							<a href="/cmc_comunicados">
							<img src="{imgComunic}"/>
							
	    <div id="box--feto--content">
	    
	    <p class="titulo-f">{detalhes}</p>
	    
	    </div></a>
	    <p class="text--data--f">Data: {dataCm}</p>
	    </div> """
							print("Feito do Municipeo")
							
						
						allDataComunic = allDataComunic +f"""
						
						
				                <div onclick="showCommunic()" class="box--comunic">
				                    <div class="comunic--head">
				
				                        <img src="{imgComunic}" alt="imgcominic" />
				                        
				                    </div>
				                    <div class="comunic--content">
				                        <div class="cmc--title">
				
				                            <h3>{tituloC}</h3>
				                            <small>📅 Data: {dataCm}</small>
	<small>🔢 Comunicado N°: {numC}</small>
				                           
				                        </div>
				                        
				                            <p>{detalhes}</p>
				                       
				                        
				
				
				                    </div>
				
				                </div>
						
						"""
		
	
	#load eventos
	allDataEvent = ""
	
	countEvs = 0
	for numEs in listIdsEvs:
		
		
		
		
		
		
		
		
		
		for cEve in resEv:
			
			evento = resEv[cEve]
			detalhesEv = evento['detalhes']
			
			numEvent = evento['numero']
			
			
			
			
			if str(numEs) == str(numEvent):
				
				print("numero encotrado 2")
						
				
				
				tituloEv = evento['titulo']
				
				numEv = evento['numero']
				
				dataPubli = evento['data']
				linkImgEv = evento["linkimg"]
				
				
				if "visi" in evento:
					resvisiEv = evento["visi"]
					
					if resvisiEv == "on" :
						statusVEv = "visiv7"
					else:
						statusVEv = "invisi7"
				else:
					statusVEv= "visiv7"
				
				if statusVEv != "visiv7":
					...
				else:
					
					if "fcac" in evento:
						
						checkFCAC = evento["fcac"]
					else:
						checkFCAC = "off"
					
					countEvs = countEvs +1
					
					if countEvs >= 4:
						break
					else:
						
						if str(checkFCAC) == "on":
							allDataFCAC = allDataFCAC + f"""<a href="/cmc_eventos">
							<div class="box--feito"><img src="{linkImgEv}"/>
							
	    <div id="box--feto--content">
	    
	    <p class="titulo-f">{detalhesEv}</p>
	    
	    </div>
	    <p class="text--data--f">Data: {dataPubli}</p>
	    </div></a> """
							print("on no envento encotrado.")
						
						allDataEvent = allDataEvent +f"""<div onclick="showEvent()" class="box--card">
						
						<h3>{tituloEv}</h3>
						<small>📅 Data: {dataPubli}</small>
	<small>🔢 Evento N°: {numEv}</small>
						 
						 
						 
						 <img src="{linkImgEv}" alt="event image" />
						
						
				        <br>
				        <p>{detalhesEv}</p>
				        
				       
				        
				        </div>
				        
				        
				        """
		
		
	
	return [allDataComunic,str(allDataEvent),allDataFCAC,infoNewEvent]



def loadComunicEventf_cac():
	
	token = get_id_token()
	
	
	
    
    
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	
	
	rotaEv = "Eventos"
	rotaCm = "Comunicados"
	
	resEv = resInfoCm[rotaEv]
	resCm = resInfoCm[rotaCm]
	
	
	
	
	#armazenar ids na lista para analizar
	
	
	listIdsEvs = []
	
	
	for cEv in resEv:
		
		eventC = resEv[cEv]
		
		numIdEv = eventC['numero']
		
		
		if numIdEv.isnumeric():
			
			listIdsEvs.append(numIdEv)
			
			
	
	listIdsCm = []
	
	
	for cCm in resCm:
		
		comuC = resCm[cCm]
		
		numIdCm = comuC['numero']
		
		
		if numIdCm.isnumeric():
			
			listIdsCm.append(numIdCm)
			
	
	
	
	
	#load comunicados
	
	listIdsCm = sorted(listIdsCm, reverse = True)
	
	listIdsEvs = sorted(listIdsEvs, reverse = True)
	
	
	print(listIdsCm)
	print(listIdsEvs)
	
	
	countCm = 0
	
	allDataComunic = ""
	for numE in listIdsCm:
		
		
		
		
		
		
		
		for cComu in resCm:
			
			
			comunicado = resCm[cComu]
			numComu = comunicado['numero']
			
			
			
			
			if str(numE) == str(numComu):
				
				print("numero encotrado")
				
				
				tituloC = comunicado['titulo']
				
				detalhes = comunicado["detalhes"]
				
				linkImg = comunicado["linkimg"]
				
				numC  = comunicado["numero"]
				
				dataCm = comunicado["data"]
				
				
				imgComunic = linkImg
				
				
				countCm = countCm +1
				
				
				if countCm >= 4:
					break
				else:
					
					allDataComunic = allDataComunic +f"""
					
					
			                <div onclick="showCommunic()" class="box--comunic">
			                    <div class="comunic--head">
			
			                        <img src="{imgComunic}" alt="imgcominic" />
			                        
			                    </div>
			                    <div class="comunic--content">
			                        <div class="cmc--title">
			
			                            <h3>{tituloC}</h3>
			                            <small>📅 Data: {dataCm}</small>
<small>🔢 Comunicado N°: {numC}</small>
			                           
			                        </div>
			                        
			                            <p>{detalhes}</p>
			                       
			                        
			
			
			                    </div>
			
			                </div>
					
					"""
	
	
	#load eventos
	allDataEvent = ""
	
	countEvs = 0
	for numEs in listIdsEvs:
		
		
		
		
		
		
		
		
		
		for cEve in resEv:
			
			evento = resEv[cEve]
			detalhesEv = evento['detalhes']
			
			numEvent = evento['numero']
			
			
			
			
			if str(numEs) == str(numEvent):
				
				print("numero encotrado 2")
						
				
				
				tituloEv = evento['titulo']
				
				numEv = evento['numero']
				
				dataPubli = evento['data']
				linkImgEv = evento["linkimg"]
				
				countEvs = countEvs +1
				
				if countEvs >= 4:
					break
				else:
					
					allDataEvent = allDataEvent +f"""<div onclick="showEvent()" class="box--card">
					
					<h3>{tituloEv}</h3>
					<small>📅 Data: {dataPubli}</small>
<small>🔢 Evento N°: {numEv}</small>
					 
					 
					 
					 <img src="{linkImgEv}" alt="event image" />
					
					
			        <br>
			        <p>{detalhesEv}</p>
			        
			       
			        
			        </div>
			        
			        
			        """
		
		
	
	return [allDataComunic,str(allDataEvent)]




def loadCommitDash(tituloev,dataev,detalheev, url_imgev):
	
	
	tituloEv = tituloev
	dataEv = dataev
	detalheEv = detalheev
	urlImageEv = url_imgev
	
	
	dataHora = str(datetime.now())
	dataHora = dataHora.split(".")[0]
	dataHora = str(dataHora)
	
	token = get_id_token()
	
	
	
	urlBase = f"{firebaseURL}/Eventos/.json?auth={token}"
	
	
	
	
	

	
	
	resGet = req.get(urlBase)
	
	resDiciEv =  resGet.json()
	listIdsEv = []
	for cEve in resDiciEv:
		
		evento = resDiciEv[cEve]
		
		numIdEv= evento['numero']
		
		if numIdEv.isnumeric():
			
			numIdInt = int(numIdEv)
			
			listIdsEv.append(numIdInt)
	
	
	lastId = max(listIdsEv)
	
	
	dataPush = {
		"detalhes": detalheEv,
		"titulo": tituloev,
		"numero": str(lastId+1),
		"data": dataHora,
		"linkimg": urlImageEv
		
	
	}
	
	
	
	
	
	
	resPush = req.post(urlBase, data = json.dumps(dataPush))
	
	print(resPush)
	
	
	
	return ".Comitou com sucesso."





def loadCommitDashCm(titulocm,datacm,detalhecm,url_imgcm,chechfeitocm):
	
	
	
	tituloCm = titulocm
	dataCm = datacm
	detalheCm= detalhecm
	urlImageCm = url_imgcm
	checkFeitoCm = str(chechfeitocm)
	
	dataHora = str(datetime.now())
	dataHora = dataHora.split(".")[0]
	dataHora = str(dataHora)
	
	token = get_id_token()
	
	
	
	urlBase = f"{firebaseURL}/Comunicados/.json?auth={token}"
	
	
	
	
	
	
	resGet = req.get(urlBase)
	
	resDiciCm =  resGet.json()
	listIdsCm = []
	for cComu in resDiciCm:
		
		comunicado = resDiciCm[cComu]
		
		numIdCm= comunicado['numero']
		
		if numIdCm.isnumeric():
			
			numIdInt = int(numIdCm)
			
			listIdsCm.append(numIdInt)
	
	
	lastId = max(listIdsCm)
	
	
	dataPush = {
		"detalhes": detalheCm,
		"titulo": tituloCm,
		"numero": str(lastId+1),
		"data": dataHora,
		"fcac": checkFeitoCm,
		"linkimg": urlImageCm,
		
	
	}
	
	
    
	
	
	resPush = req.post(urlBase, data = json.dumps(dataPush))
	
	#print(resPush)
	
	if resPush.status_code == 200:
		
		print("comunicado Enuciado")
		return "Enuciado comunicado com sucesso..."
	else:
		
		print("falha ao comunicar")
		return "Erro ao Enuciar o Conicado , coctante a BSoft Tecnology"


# funcao que deleta eventos e comunicados
def dellInfoNewsCMC(tpinfo, idinfo):
	
	typeInfo = tpinfo
	idInfo = idinfo
	
	token = get_id_token()
	
	
	
	
	
	urlBase = f"{firebaseURL}/"
	
	rota = ""
	if typeInfo == "Comunicado":
		rota = "Comunicados"
	elif typeInfo == "Evento":
		
		rota = "Eventos"
	urlBase = urlBase+rota+"/.json?auth={token}"
	
	
	resInfo = req.get(urlBase)
	
	
	resInfo = resInfo.json()
	msgRes = ["nao","Teve Problemas Ao Eliminar"]
	for cNewsCMC in resInfo:
		
		infocmc = resInfo[cNewsCMC]
		
		numId =  infocmc['numero']
		
		
		if str(numId) == str(idInfo):
			
			
			urlDellInfo = f"{firebaseURL}/{rota}/{cNewsCMC}/.json?auth={token}"
			
			
			resDellInfo = req.delete(urlDellInfo)
			
			if resDellInfo.status_code == 200:
				msgRes = ["sim","Eliminado com sucesso."]
			else:
				...
			
			break
		
		
	
	
	
	
	return msgRes



def loadSearchevcm(dadoPesq, typeSearch):
	
	token = get_id_token()
	
	
	
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	tpS = typeSearch
	
	resInfoCm = req.get(urlBase)
	
	resInfoCm = resInfoCm.json()
	
	
	
	
	
	rotaEv = "Eventos"
	rotaCm = "Comunicados"
	
	resEv = resInfoCm[rotaEv]
	resCm = resInfoCm[rotaCm]
	
	
	
	
	#armazenar ids na lista para analizar
	
	infoNewEvent = []
	listIdsEvs = []
	
	
	for cEv in resEv:
		
		eventC = resEv[cEv]
		
		numIdEv = eventC['numero']
		
		
		if numIdEv.isnumeric():
			
			listIdsEvs.append(numIdEv)
			
			
	
	listIdsCm = []
	
	
	for cCm in resCm:
		
		comuC = resCm[cCm]
		
		numIdCm = comuC['numero']
		
		
		if numIdCm.isnumeric():
			
			listIdsCm.append(numIdCm)
			
	
	
	
	
	#load comunicados
	
	listIdsCm = sorted(listIdsCm, reverse = True)
	
	listIdsEvs = sorted(listIdsEvs, reverse = True)
	
	
	print(listIdsCm)
	print(listIdsEvs)
	
	
	countCm = 0
	allDataFCAC = ""
	allDataComunic = ""
	for numE in listIdsCm:
		
		
		
		
		
		
		
		for cComu in resCm:
			
			
			comunicado = resCm[cComu]
			numComu = comunicado['numero']
			
			
			
			
			
			if str(numE) == str(numComu):
				
				print("numero encotrado")
				
				
				tituloC = comunicado['titulo']
				
				detalhes = comunicado["detalhes"]
				
				linkImg = comunicado["linkimg"]
				
				numC  = comunicado["numero"]
				
				dataCm = comunicado["data"]
				
				
				if str(numComu) == listIdsCm[0]:
					
					infoNewEvent.append(tituloC)
					infoNewEvent.append(numC)
					infoNewEvent.append(dataCm)
					infoNewEvent.append(linkImg)
					infoNewEvent.append(detalhes)
					
					
					
				
				if "fcac" in comunicado:
					checkFCAC = comunicado["fcac"]
				else:
					checkFCAC = "off"
				
				imgComunic = linkImg
				
				
				countCm = countCm +1
				
				
				if countCm >= 4:
					break
				else:
					
					listDadoPesq = dadoPesq.split(" ")
					
					for cPalavra in listDadoPesq:
						lengthP = len(cPalavra)
						if lengthP <= 4:
							continue
						else:
							
							if cPalavra.lower() in tituloC.lower():
								if str(checkFCAC) == "on":
								
									allDataFCAC = allDataFCAC + f"""
									<div class="box--feito"><img src="{imgComunic}"/>
									
			    <div id="box--feto--content">
			    
			    <p class="titulo-f">{detalhes}</p>
			    
			    </div
			    <p class="text--data--f">Data: {dataCm}</p>
			    </div> """
									print("Feuto do Municipeo")
									
								
								allDataComunic = allDataComunic +f"""
								
								
						                <div onclick="showCommunic()" class="box--comunic">
						                    <div class="comunic--head">
						
						                        <img src="{imgComunic}" alt="imgcominic" />
						                        
						                    </div>
						                    <div class="comunic--content">
						                        <div class="cmc--title">
						
						                            <h3>{tituloC}</h3>
						                            <small>📅 Data: {dataCm}</small>
			<small>🔢 Comunicado N°: {numC}</small>
						                           
						                        </div>
						                        
						                            <p>{detalhes}</p>
						                       
						                        
						
						
						                    </div>
						
						                </div>
								
								"""
					
								break
	
	
	#load eventos
	allDataEvent = ""
	
	countEvs = 0
	for numEs in listIdsEvs:
		
		
		
		
		
		
		
		
		
		for cEve in resEv:
			
			evento = resEv[cEve]
			detalhesEv = evento['detalhes']
			
			numEvent = evento['numero']
			
			
			
			
			if str(numEs) == str(numEvent):
				
				print("numero encotrado 2")
						
				
				
				tituloEv = evento['titulo']
				
				numEv = evento['numero']
				
				dataPubli = evento['data']
				linkImgEv = evento["linkimg"]
				
				if "fcac" in evento:
					
					checkFCAC = evento["fcac"]
				else:
					checkFCAC = "off"
				
				countEvs = countEvs +1
				
				
				
				listDadoPesq = dadoPesq.split(" ")
				
				if countEvs >= 4:
					break
				else:
					
					
					for cPalavraEv in listDadoPesq:
						if cPalavraEv.lower() in tituloEv.lower():
							
									
							
							if str(checkFCAC) == "on":
								allDataFCAC = allDataFCAC + f"""
								<div class="box--feito"><img src="{linkImgEv}"/>
								
		    <div id="box--feto--content">
		    
		    <p class="titulo-f">{detalhesEv}</p>
		    
		    </div
		    <p class="text--data--f">Data: {dataPubli}</p>
		    </div> """
								print("on no envento encotrado.")
							
							allDataEvent = allDataEvent +f"""<div onclick="showEvent()" class="box--card">
							
							<h3>{tituloEv}</h3>
							<small>📅 Data: {dataPubli}</small>
		<small>🔢 Evento N°: {numEv}</small>
							 
							 
							 
							 <img src="{linkImgEv}" alt="event image" />
							
							
					        <br>
					        <p>{detalhesEv}</p>
					        
					       
					        
					        </div>
					        
					        
					        """
		
		
	
	
	if tpS == "cm":
		return [allDataComunic]
	else:
		return [allDataEvent]
	
	
	


def sendMensageCMC(nome,tel,email,msg):
	
	
	dataHora = str(datetime.now())
	dataHora = dataHora.split(".")[0]
	dataN,horaN = dataHora.split(" ")
	print(dataN)
	print(horaN)
	
	token = get_id_token()
	
	
    
    
	
	
	urlBase = f"{firebaseURL}/Mensagens/.json?auth={token}"
	
	
	
	resGetMsg = req.get(urlBase)
	resGetMsg = resGetMsg.json()
	
	listIdsMsg = []
	
	for cMsg in resGetMsg:
		
		msgBase = resGetMsg[cMsg]
		
		idMsg = msgBase["numero"]
		
		listIdsMsg.append(int(idMsg))
	
	lastId = max(listIdsMsg)
		
	newNumId = str(int(lastId)+1)
	
	
	dataPushMsg = {
		"nome": nome,
		"data": dataN,
		"hora": horaN,
		"email": email,
		"msg": msg,
		"tell": tel,
		"numero": newNumId,
		"nova": "1",
		
		
	
	}
	
	
	
	resPushmsg = req.post(urlBase, data = json.dumps(dataPushMsg))
	
	
	if resPushmsg.status_code == 200:
		return ["sim"]
	else:
		return ["nao"]



def dellInfoNewsCMCMsg(typeInfoMsg,numIdInfoMsg):
	print("msg start")
	print(typeInfoMsg)
	print(numIdInfoMsg)
	
	token = get_id_token()
	
	
    
	
	urlBase = f"{firebaseURL}/Mensagens/.json?auth={token}"
	
	resMsg = req.get(urlBase)
	
	
	resMsg = resMsg.json()
	
	
	resMsgdl = "nao"
	
	for cMsg in resMsg:
		
		
		msgdl = resMsg[cMsg]
		
		
		numIdMsg = msgdl["numero"]
		
		
		if str(numIdMsg) == str(numIdInfoMsg):
			
			#print("Mensagem para Eliminacao encotrada")
			
			
			
			
			urldlmsg = f"{firebaseURL}/Mensagens/{cMsg}/.json?auth={token}"
			
			resdlMsg = req.delete(urldlmsg)
			
			
			if resdlMsg.status_code == 200:
				resMsgdl = "sim"
			else:
				...
			
			
	
	print("msg and")
	
	
	return [resMsgdl]


def AtzInfoNewsCMCVsi(typeInfoVsi,numIdInfoVsi):
	
	token = get_id_token()
	
	
    
    
	
	urlBase = f"{firebaseURL}/.json?auth={token}"
	
	
	resGetAtz = req.get(urlBase)	
	
	resGetAtz = resGetAtz.json()
	
	#header da da atualizacao
	
	
	rotaCm = "Comunicados"
	rotaEv = "Eventos"
	
	
	resAtzEv = resGetAtz[rotaEv]
	resAtzCm = resGetAtz[rotaCm]
	
	#print(typeInfoVsi, "**************")
	
	
	backRes = "nao"
	newNBtn = ""
	
		
	if typeInfoVsi == "comunicado":
		#print("*/*****E um comunicado")
		for cAtzCm in resAtzCm:
			
			comuAtzCm = resAtzCm[cAtzCm]
			
			numIdBase = comuAtzCm["numero"]
			
			
			if str(numIdBase) == str(numIdInfoVsi):
				#print("Esse é o Comunicado a Ser Atualizado para escondido =============")
				urlAtzCm = f"{firebaseURL}/Comunicados/{cAtzCm}/.json?auth={token}"
				
				
				if "visi" in comuAtzCm:
					resAtzCmVsi = comuAtzCm["visi"]
					
					if resAtzCmVsi == "on":
						statusVAtzCm = "vsion"
					else:
						statusVAtzCm = "vsioff"
				else:
					statusVAtzCm = "vsion"
				
				
				
				
				if statusVAtzCm == "vsion":
					dataPAtzCm = {
					"visi": "off"
					
					
					}
					
					newNBtn = "Invisivel"
				else:
					
					dataPAtzCm = {
					"visi": "on"
					
					
					}
					newNBtn = "Visivel"
				
				
					
				
				resVsiAtzCm = req.patch(urlAtzCm, data = json.dumps(dataPAtzCm))
				
				
				if resVsiAtzCm.status_code == 200:
					
					#print("Escondido com Sucesso.")
					backRes = "sim"
				
				
				
				
				
				
				
				break
				
			
		
	
	
	
	if typeInfoVsi == "evento":
		#print("*/*****E um Evento")
		for cAtzEv in resAtzEv:
			
			eventAtzEv = resAtzEv[cAtzEv]
			
			numIdBaseEv = eventAtzEv["numero"]
			
			
			if str(numIdBaseEv) == str(numIdInfoVsi):
				#print("Esse é o Evento a Ser Atualizado para escondido =============")
				urlAtzEv = f"{firebaseURL}/Eventos/{cAtzEv}/.json?auth={token}"
				
				
				if "visi" in eventAtzEv:
					resAtzEvVsi = eventAtzEv["visi"]
					
					if resAtzEvVsi == "on":
						statusVAtzEv = "vsion"
					else:
						statusVAtzEv = "vsioff"
				else:
					statusVAtzEv = "vsion"
				
				
				
				
				if statusVAtzEv == "vsion":
					dataPAtzEv = {
					"visi": "off"
					
					
					}
					
					newNBtn = "Invisivel"
				else:
					
					dataPAtzEv = {
					"visi": "on"
					
					
					}
					newNBtn = "Visivel"
				
				
					
				
				resVsiAtzEv = req.patch(urlAtzEv, data = json.dumps(dataPAtzEv))
				
				
				if resVsiAtzEv.status_code == 200:
					
					print("Atualizado com Sucesso.")
					backRes = "sim"
				
				
				
				
				
				
				
				break
				
			
		
	
	
	
	
	
	
	return [backRes,newNBtn]

def doReadedMsgCMC(msgF):
	
	token = get_id_token()
	
	
	
	urlBase = f"{firebaseURL}/Mensagens/.json?auth={token}"
	
	
	resM = req.get(urlBase)
	
	resM = resM.json()
	
	#header para atualizacao da mensagem
	
	
	
	for cMsg in resM:
		
		msg = resM[cMsg]
		
		#print("todas  mensagens ",len(msg))
		
		
		enova = msg["nova"]
		
		if str(enova) == "1":
			
			print("E uma nova")
			
			urlBaseReaded = f"{firebaseURL}/Mensagens/{cMsg}/.json?auth={token}"
			dpush = {
				"nova": "0"
			}
			resMR = req.patch(urlBaseReaded, data = json.dumps(dpush))
			
			print(resMR.status_code)
			
			
		else:
			print("é mensagem antiga")
	
	
	
	
	
	
	return ["sim"]





app = Flask(__name__)


app.secret_key = "chave_super_secreta_123"





@app.route('/')
def home():
    
    
    allDataCE = loadComunicEvent()
    
    dataEvent = allDataCE[1]
    dataFCAC = allDataCE[2]
    dataComunic = allDataCE[0]
    
    
    return render_template("index.html", pEvent = dataEvent, pComunic = dataComunic,pFCAC = dataFCAC)

# Verifica se há algo como isso:
@app.route('/cmc_comunicados')
def eventos_comunicados():
    
    allDataCE = loadComunic()
    
    dataComunic = allDataCE[0]
    
    infoNewComu = allDataCE[1]
    
    
    
    
    return render_template("comunicados.html", pComunic = dataComunic,infoNewCm = infoNewComu)


# Verifica se há algo como isso:
@app.route('/cmc_eventos')
def eventosCmc():
    
    allDataCE = loadEvent()
    
    dataEvent = allDataCE[0]
    
    infoNewComu = allDataCE[1]
    
    
    
    
    return render_template("eventos.html", pEvent = dataEvent,infoNewCm = infoNewComu)



@app.route("/historia")
def historiaChimoio():
	
	
	return render_template("historiadacidade.html")

@app.route("/sobre_nos")
def sobreNos():
	
	
	return render_template("sobre.html")

@app.route("/contatos",methods=["GET","POST"])
def contatos():
	
	dataEmail = request.args.get("dataemail")
	
	if request.method == "POST":
		
		print("Metodo Post: Encotrado...")
		nome = request.form.get("nomeusr")
		tel = request.form.get("tellusr")
		
		email = request.form.get("emailusr")
		
		msg = request.form.get("msgusr")
		
		
		resMSG  = sendMensageCMC(nome,tel,email,msg)
		
		if resMSG[0] == "sim":
			return render_template("contacto.html", dataemail = dataEmail,msgSend = "Mensagem Enviada com sucesso.")
			
			
		
		
	
	return render_template("contacto.html", dataemail = dataEmail)
	

#funcao de roprotecao de acesso do admin

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin_logado"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated_function



@app.route("/CNdashboard12")
@login_required
def dash_cmc():
    allDataCE =  loadDashCMC()
    dataEvent = allDataCE[1]
    dataComunic = allDataCE[0]
    dataMsg = allDataCE[2]
    dataLen = allDataCE[3]
    
    
    dataStatus = allDataCE[4]
    
    numNewMsg = dataStatus[0]
    pVisiveis = str(dataStatus[1])
    pInvisiveis = str(dataStatus[2])
    pTotal = int(pVisiveis) +int(pInvisiveis)
    
    
    dataAgora = datetime.now()
    
    dataAgora = str(dataAgora).split(" ")[0]
    
    
    
    numEv = dataLen[0]
    numCm = dataLen[1]
    numMsg = dataLen[2]
    
    return render_template("dashcmc.html", pEvent = dataEvent, pComunic = dataComunic, nEvent = numEv,nMsg = numMsg,pMsg = dataMsg,numNewMsg= numNewMsg, nComu = numCm, plVisi = pVisiveis, plInvi = pInvisiveis, plTotal = pTotal,dataAg = dataAgora )




@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":
        
        print("o post foi achado __f_")
        username = request.form.get("username")
        password = request.form.get("password")

        # CREDENCIAIS FIXAS (pode trocar por BD depois)
        if username == usercn and password == passwordcn:
            session["admin_logado"] = True
            return redirect("/CNdashboard12")

        return render_template(
            "login_dash.html",
            erro="Credenciais inválidas"
        )

    return render_template("login_dash.html")


# funcao de logaut da adimin

@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


@app.route("/commitEvent_cmc", methods=["POST"])
def loadCommitEvent():
	
	
	tEv= request.form.get("tituloev")
	dEv = request.form.get("dataev")
	detaEv = request.form.get("detalheev")
	dataImageEv = request.files.get("imageev")
	
	if not dataImageEv:
		print("sem nehuma imagem")
		
		return ["Erro ao publicar , Imagem nao Encotrada..."]
	else:
		print("Imagem do Evento Encotrado.")
		
		
		result_upload_clEv = cloudinary.uploader.upload(dataImageEv)
		
		url_imageEv = result_upload_clEv.get("secure_url")
		
		
		resCDash = loadCommitDash(tEv,dEv,detaEv, url_imageEv)
		
		
		return ["Evento Publicado co  sucesso"]
	
	
	
	
	
	
	return ["Erro Ao Publicar o Evento..."]



@app.route("/commitComunic_cmc", methods=["POST"])
def loadCommitComunic():
	
	tCm = request.form.get("titulocm")
	dCm = request.form.get("datacm")
	detaCm = request.form.get("detalhecm")
	
	checkFeito_cmc = request.form.get("checkbtncm")
	
	dataImageCm = request.files.get("imagecm")
	
	
	
	
	
	if not dataImageCm:
		
		Notf = "Para enuciar, Adicione uma imagem sobre comunicado a enuciar..."
		print(dataImageCm)
		print(checkFeito_cmc)
		return jsonify([Notf])
	else:
		print("Imagem Encotrada")
		
		#print(checkFeito_cmc)
		
		result_upload_cl = cloudinary.uploader.upload(dataImageCm)
		
		url_image = result_upload_cl.get("secure_url")
		
		
		resCDashCm= loadCommitDashCm(tCm,dCm,detaCm, url_image,checkFeito_cmc)
		
		print("Imagem armazenada...")
	
	
	
	
	
	
	return jsonify(["O Comunicado  foi Enuciado ..."])


@app.route("/dellinfo", methods = ["POST"])
def dellInfoCMC():
	
	data = request.get_json()
	
	typeInfo = data.get('typeinfocmc')
	numIdInfo = data.get('numeroinfocmc')
	
	
	
	resDell = dellInfoNewsCMC(typeInfo,numIdInfo)
	
	if resDell[0] == "sim":
		
		return jsonify([resDell[0],typeInfo])
	else:
		
		return jsonify([resDell[0],typeInfo])


@app.route("/readed_cmcmsg", methods = ["POST"])
def doReadedCMCMsg():
	
	msgF  = request.form.get("msg")
	
	
	
	
	
	resMsgF = doReadedMsgCMC(msgF)
	
	return jsonify([msgF])








@app.route("/dellinfomsg", methods = ["POST"])
def dellInfoCMCMsg():
	
	data = request.get_json()
	
	typeInfoMsg = data.get('typeinfocmcmsg')
	numIdInfoMsg = data.get('numeroinfocmcmsg')
	
	
	
	resDellMsg = dellInfoNewsCMCMsg(typeInfoMsg,numIdInfoMsg)
	
	if resDellMsg[0] == "sim":
		
		return jsonify([resDellMsg[0],typeInfoMsg])
	else:
		
		return jsonify([resDellMsg[0],typeInfoMsg])


@app.route("/atualizationinfovsi", methods = ["POST"])
def atualizationInfoCMCVsi():
	
	data = request.get_json()
	
	typeInfoVsi = data.get('typeinfocmcvsi')
	numIdInfoVsi = data.get('numeroinfocmcvsi')
	
	
	
	resAtzVsi = AtzInfoNewsCMCVsi(typeInfoVsi,numIdInfoVsi)
	
	if resAtzVsi[0] == "sim":
		
		return jsonify([resAtzVsi[0],typeInfoVsi,resAtzVsi[1]])
	else:
		
		return jsonify([resDellMsg[0],typeInfoVsi,resAtzVsi[1]])



@app.route("/loadsearchcmcev", methods = ["POST"])
def searchEv():
	
	
	
	data = request.get_json()
	
	dadoPesq = data.get("dadopesq")
	
	
	resPesq = loadSearchevcm(dadoPesq,"ev")
	
	dataEvq = resPesq[0]
	return jsonify([dataEvq])



@app.route("/loadsearchcmccm", methods = ["POST"])
def searchCm():
	
	
	
	data = request.get_json()
	
	dadoPesq = data.get("dadopesq")
	
	
	resPesq = loadSearchevcm(dadoPesq,"cm")
	dataCmq = resPesq[0]
	
	return jsonify([dataCmq])





@app.route("/proceguirmail", methods = ["POST"])
def proceguirMail():
	
	
	
	data = request.get_json()
	
	inDadoMail= data.get("indadopesq");
	
	if "@" in  inDadoMail:
		
		print("tem @")
		lData = inDadoMail.split("@")
		
		if len(lData[0]) <= 3:
			print("nome do email menor")
			...
		else:
			print("redirecionamento funcionando...")
			return jsonify({"redirect": url_for("contatos", dataemail = inDadoMail)})
			
			
	
	return jsonify({"erro":f"Email Invalido"})






	


@app.route("/politicas")
def politicasPrivacidade():
	
	
	return render_template("politicaseprivacidade.html")
	

@app.route('/countVisit', methods=['POST'])
def count_visit():
	token = get_id_token()
	hoje = date.today().isoformat()
	url = f"{firebaseURL}/stats/total_visitas/{hoje}.json?auth={token}"
	# obter valor atual
	res = req.get(url)
	atual = res.json() or 0
	# atualizar
	req.put(url, json=atual + 1)
	return '', 204
	
@app.route('/newToday', methods=['POST'])
def visitante_unico():
	token = get_id_token()
	hoje = date.today().isoformat()
	url = f"{firebaseURL}/stats/visitantes_unicos/{hoje}.json?auth={token}"
	res = req.get(url)
	
	atual = res.json() or 0
	req.put(url, json=atual + 1)
	return jsonify({"status": "ok"})



@app.route('/updateinfodash', methods=['POST'])
def update_info_dash():
    allDataCE =  loadDashCMC()
    dataEvent = allDataCE[1]
    dataComunic = allDataCE[0]
    dataMsg = allDataCE[2]
    dataLen = allDataCE[3]
    
    
    dataStatus = allDataCE[4]
    
    numNewMsg = dataStatus[0]
    pVisiveis = str(dataStatus[1])
    pInvisiveis = str(dataStatus[2])
    pTotal = int(pVisiveis) +int(pInvisiveis)
    
    
    dataAgora = datetime.now()
    
    dataAgora = str(dataAgora).split(" ")[0]
    
    
    
    numEv = dataLen[0]
    numCm = dataLen[1]
    numMsg = dataLen[2]
    
    print("Atualizaxao do Dash")
    return jsonify([numEv,
                              numCm,
                              numMsg,
                              numNewMsg])




@app.route('/stats/week/unicos')
def stats_week_unicos():
    return gerar_stats_semanais('visitantes_unicos')

@app.route('/stats/week/total')
def stats_week_total():
    return gerar_stats_semanais('total_visitas')


@app.route("/test-firebase")
def test_firebase():
    token = get_id_token()

    

    url = f"{firebaseURL}/.json?auth={token}"

    r = req.get(url)

    return str(r.json())


def gerar_stats_semanais(tipo):
    hoje = datetime.now()
    dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']

    labels = []
    valores = []
    token = get_id_token()
    
    
    for i in range(6, -1, -1):
        dia = hoje - timedelta(days=i)
        data_str = dia.strftime('%Y-%m-%d')

        labels.append(dias_semana[dia.weekday()])
        
        url = f"{firebaseURL}/stats/{tipo}/{data_str}.json?auth={token}"
        res = req.get(url)
        valor = res.json() if res.ok and res.json() else 0

        valores.append(valor)

    return jsonify({
        "labels": labels,
        "data": valores
    })

app.run(debug="True")