import urllib.request
import json

#test
#test

guid = "5336ccd0-a833-40b7-ab39-ada7511db97f" #GUID para llamar al JSON de Microsoft (lo requiere)
latestVersion = "0000000000" #Version inicial del JSON de Microsoft 
							 #(es para saber si necesitas traerlo de nuevo o no)
							 #Revisar, esto habria que traerlo de algun archivo.
							 #Asi como esta, va a traer todo de nuevo todo el tiempo
ws = "https://endpoints.office.com"

#Primero chequeamos si necesitamos o no traer las IP
#Si no hay dif entre latestVersion y la version aca, no traemos

#armamos la peticion
requestPath = ws+'/'+'version'+'/'+'Worldwide'+'?ClientRequestId='+guid
o365Version = json.loads(urllib.request.urlopen(requestPath).read())['latest']
#Comparamos latestVersion con la version que nos trajimos
if latestVersion < o365Version:
	#la version que tenemos es menos reciente que la que trajimos
	latestVersion = o365Version
	print(latestVersion)
else:
	#la version que tenemos es igual o mas reciente
