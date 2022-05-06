import uuid
import json
import ssl
import requests


debug = 1

# Funcion para hacer los llamados a O365
# 	method: version: trae versiones; endpoints: trae urls/ips
# 	scope: Worldwide: todos. No vamos a usar otro, pero conviene dejarlo asi
def urlHelper(method,scope):
	ws = "https://endpoints.office.com"
	guid = str(uuid.uuid4())
	requestPath = ws+'/'+method+'/'+scope+'?ClientRequestId='+guid
	return requests.get(requestPath).text

# Funcion para ver si necesitamos actualizar
# latestVersion: ultima version registrada por el applet
def checkVersion():
	return json.loads(urlHelper("version","Worldwide"))['latest']

# Funcion para traernos las IP de O365
def getIps():
	return json.loads(urlHelper("endpoints","Worldwide"))

# Funcion para traer el data group entero del F5
def getDataGroup(host,dataGroup,user,passwd,verify):
	requestPath = 'https://'+host+'/mgmt/tm/ltm/data-group/internal/'+dataGroup
	return json.loads(requests.get(requestPath,verify,auth=(user, passwd)).text)

# TODO: Funcion para meter las IP en el datagroup
