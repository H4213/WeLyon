import json
import urllib
import os
import sys
import threading
sys.path.append("../")

import service

from src.model import Velov

#constants
VELOV_DATA_SOURCE = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"

#Prends en argument l'url du fichier json concernant les donnees de velov
#ex: "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"

def createVelovTable(urlSource) :
	service.logMessage(".Loading of json from the server Velov ")
	urllib.urlretrieve(urlSource, "velov.json")
	json_file = open('velov.json')

	data = json.load(json_file)
	listVelov = []
	service.logMessage(".Parsing the json file")
	for i in  range(0, 10):
	#data["nb_results"]
		idUser = 1
		title = "Velov de " + data["values"][i][2]
		if data["values"][i][11]=="OPEN":
			description = "Etat : " + "OUVERT"
		else:
			description = "Etat : " + "FERME"
		lat = data["values"][i][8]
		lnd = data["values"][i][9]
		
		obj = Velov(title, lnd, lat, idUser, [], description)
		obj.libre = data["values"][i][12]
		obj.velo = data["values"][i][13]

		obj.idVelov = data["values"][i][17]
		listVelov.append(obj);

	json_file.close()
	os.remove('velov.json')
	
	return listVelov
	



#rafraichit ou ajoute les donnees dans la base
def refreshVelovData(urlSource):
	list = createVelovTable(urlSource)
	service.logMessage(".Updating the database")
	for v in list:
		service.updateVelovByIdVelov(v)
	service.logMessage(".Velo'v is up to date")
	
#lance le rafraichissement periodique des donnees velov
def start_velov_data(tempo = 60.0):
	refreshVelovData(VELOV_DATA_SOURCE)
	threading.Timer(tempo, start_velov_data, [tempo]).start()
	