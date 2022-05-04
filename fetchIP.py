import urllib.request
import uuid
import json

debug = 1

# Funcion para hacer los llamados a O365
# 	method: version: trae versiones; endpoints: trae urls/ips
# 	scope: Worldwide: todos. No vamos a usar otro, pero conviene dejarlo asi
def urlHelper(method,scope):
	ws = "https://endpoints.office.com"
	guid = str(uuid.uuid4())
	requestPath = ws+'/'+method+'/'+scope+'?ClientRequestId='+guid
	return urllib.request.urlopen(requestPath).read()

# Funcion para ver si necesitamos actualizar
# latestVersion: ultima version registrada por el applet
# Devuelve True si necesita actualizar, False de lo contrario
def checkVersion():
	return json.loads(urlHelper("version","Worldwide"))['latest']

# Funcion para traernos las IP de O365
def getIps():
	return json.loads(urlHelper("endpoints","Worldwide"))