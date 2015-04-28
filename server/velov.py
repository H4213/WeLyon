import json
import urllib
import os
import sys

sys.path.append("../")

import service

from src.model import Velov

#Prends en argument l'url du fichier json concernant les donnees de velov
#ex: "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"

def refreshVelovData(urlSource) :
	urllib.urlretrieve(urlSource, "velov.json")
	json_file = open('velov.json')

	data = json.load(json_file)
	listVelov = []
	for i in  range(0, data["nb_results"]):
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
		listVelov.append(obj);

	json_file.close()
	os.remove('velov.json')
	
	return listVelov
	
list = refreshVelovData("https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json");
for v in list:
	service.addPin(v)