
import facebook
import json
import datetime
import sys
<<<<<<< HEAD
=======
import urllib
import urlparse
import subprocess
>>>>>>> origin/Dev-Facebook
import requests
sys.path.append("../")

import service

from src.model import FacebookPin

def createFacebookTable() :

<<<<<<< HEAD
	# FACEBOOK_APP_ID     = '1620948188142851'
	# FACEBOOK_APP_SECRET = '52762f86fefa57c8f828617d15625169'
=======
	FACEBOOK_APP_ID     = '1620948188142851'
	FACEBOOK_APP_SECRET = '52762f86fefa57c8f828617d15625169'
>>>>>>> origin/Dev-Facebook

	# payload = {'grant_type': 'client_credentials', 'client_id': FACEBOOK_APP_ID, 'client_secret': FACEBOOK_APP_SECRET }
	# file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
	# #print file.text #to test what the FB api responded with    
<<<<<<< HEAD
	token = 'CAACEdEose0cBALvmV9HpdEt3LjuajMwGZC5YU2psFqAGxHACDETMBKqi3KY7yZAVzyXgYvcnZCpLwuxkAHECALB6yHoaScthtoldSknu3hXAdrfpVMZALbCQEm8zZAZBY67UZCoEE1pkS7iuCuk86WmhCAIDqCkdjATsKF2fpy0A6Lv1feV4um3RlaeDZBq9KnCbJaGqMIcaHsizH6q9zgfZB'
=======
	token = 'CAACEdEose0cBAKL9ZBMtAT8beNYBYnVegW2EYKAZCIRIrmMeqdsNv50m0uH5bgp7PAkwOYtzQG2qxAvHhb3gCqehrv5aygeeZAyMPTXmXokymoAleUWkuYDZC0Fut7plEDs3gAIA4WD3PHgufNyBlW9jNmNJRmAGcNhbOAjwT897vhgG5nJsOUM7ZArZCp7VZAyJRdvZAt0GwbuEpSiSZB0FT'
>>>>>>> origin/Dev-Facebook

	# # Trying to get an access token. Very awkward.
	# oauth_args = dict(client_id     = FACEBOOK_APP_ID, client_secret = FACEBOOK_APP_SECRET, grant_type    = 'client_credentials')
	# oauth_curl_cmd = ['curl','https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
	# oauth_response = subprocess.Popen(oauth_curl_cmd,stdout = subprocess.PIPE,stderr = subprocess.PIPE).communicate()[0]

	# try:
	#     token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
	# except KeyError:
	#     print('Unable to grab an access token!')
	#     exit()

	#token = 'CAACEdEose0cBAPfoaH5UtoC3nt4KYqNShODlAJyOh71QPX4FLKFldn1Tw44wu95CdtMm96gnvPkUkJGPIhsuUtzvNDncxmLrcWGA64ZCULx0GYOGmbZBS9s1jjLqg7ZB9PAaxK26XwtEgIPvciuJySZAF93FLzuBvjNUU4ANB2rQm8VnhNZCOoDjb8JDKjYiU6Q8yMMaNGoQuKFpFx8Q1'
<<<<<<< HEAD
	nbEvent=100
=======
	nbEvent=30
>>>>>>> origin/Dev-Facebook
	latitudeMin=45.6389404
	longitudeMin=4.7530973
	latitudeMax=46.2276655
	longitudeMax=5.0036580
	graph = facebook.GraphAPI(token)

	t=graph.request("search",{ 'q' : 'Villeurbanne', 'type' : 'event', 'limit' : nbEvent, 'start_time' : 'currentTime'})
	events = json.dumps(t['data'],[0], indent=1)
	i=-1
	listFacebook =[]
	nbIter = nbEvent-1
	while i < nbIter:
		
		i+=1

		title=t['data'][i]['name']

		idEvent=t['data'][i]['id']
		print(idEvent)
		try :
			Event=graph.request(idEvent)
			if 'venue' in Event:
				venue=Event['venue']
				if 'latitude' in venue:
					latitude=Event['venue']['latitude']
					longitude=Event['venue']['longitude']
					if (latitude>latitudeMin) & (longitude >longitudeMin) & (latitude <latitudeMax) & (longitude<longitudeMax) :
						if 'description' in Event:
							description = Event['description']
						else:
							description =""
						if 'start_time' in Event:
							print("start")
							start_time=Event['start_time']
							if 'end_time' in Event:
							
								end_time = Event['end_time']
							else:
								 end_time = 'currentTime'
<<<<<<< HEAD
							#image=graph.request(idEvent+'/picture?redirect=false')
							#linkpicture=image['data']['url']
							idUser=1
=======
							image=graph.request(idEvent+'/picture?redirect=false')
							linkpicture=image['data']['url']
							idUser=2
>>>>>>> origin/Dev-Facebook
							obj = FacebookPin(title, longitude, latitude, idUser, [], description)
							obj.dateBegin = start_time
							obj.dateEnd = end_time
							print (idEvent)
							obj.idFacebook = idEvent
							listFacebook.append(obj)
							print("Ok")
<<<<<<< HEAD
		except (requests.ConnectionError , urllib2.URLError):
=======
		except requests.ConnectionError:
>>>>>>> origin/Dev-Facebook
			print ("ConnectionError")
		
			


	return listFacebook

def refreshFacebookData():
	list = createFacebookTable()
	print("[LOG] Updating the database")
	for v in list:
		service.updateFacebookByIdFacebook(v)
	print("[LOG] Facebook Pins are up to date")












	# if "location" in t['data'][i] :
	# 	location = t['data'][i]['location']
	# 	locationTab=graph.request("search",{ 'q' : location,'type' : 'page'})
	# 	locationJson = json.dumps(locationTab['data'],[0], indent=1)
	# 	with open("C:\Test\Test2"+str(i)+".txt", 'w+') as myfile:
	# 		myfile.write(locationJson)
	# 		myfile.close()
	# 	json_size = len(locationJson)
	# 	j=-1
	# 	while j<json_size:
	# 		j+=1
	# 		locationName=locationTab['data'][j]['name']
	# 		if locationName == location:
	# 			truc=locationTab['data'][j]
	# 			break
	# 	idLocation = locationTab['data'][j]['id']

	# 	placeTab=graph.request(idLocation)
	# 	latitude=placeTab['location']['latitude']
	# 	longitude=placeTab['location']['longitude']

	# 	placeJson=json.dumps(placeTab)
	# 	with open("C:\Test\Test2"+str(i)+"1.txt", 'w+') as myfile:
	# 		myfile.write(placeJson)
	# 		myfile.close()

		