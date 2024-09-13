import uuid
import json
import requests # type: ignore



# Funcion para hacer los llamados a O365
# 	method= version: trae versiones; endpoints= trae urls/ips
# 	scope= Worldwide: todos. No vamos a usar otro, pero conviene dejarlo asi
# Helper function to build calls to O365
#	method= version pull versions; method= endpoints pulls urls/ips JSON
#	scope= Worlwide: everything. We do not use other than that.
def urlHelper(method: str,scope: str) -> str:
	ws = "https://endpoints.office.com"
	guid = str(uuid.uuid4())
	requestPath = ws+'/'+method+'/'+scope+'?ClientRequestId='+guid
	return requests.get(requestPath).text

# Funcion para obtener la ultima version del archivo JSON de MS
# Function to get latest version of the MS JSON File
def checkVersion() -> str:
	return json.loads(urlHelper("version","Worldwide"))['latest']

# Funcion para traernos las IP de O365
def getIps() -> list:
	return json.loads(urlHelper("endpoints","Worldwide"))

# Funcion para traer el data group entero del F5
# Era necesaria en otra version del script, pero ya no se utiliza
# La dejo por si en un futuro sirve
# Deprecated function to get whole data group from F5
# Leaving it just in case
def getDataGroup(host: str,dataGroup:str ,user: str,passwd: str,verify: bool) -> str:
	requestPath = 'https://'+host+'/mgmt/tm/ltm/data-group/internal/'+dataGroup
	return json.loads(requests.get(requestPath,verify = verify,auth=(user, passwd)).text)

# Funcion para subir el datagroup al F5
# Function to patch datagroup to F5
def patchDataGroup(host: str,dataGroup: str,user: str,passwd: str,verify: bool,records: list) -> str:
	requestPath = 'https://'+host+'/mgmt/tm/ltm/data-group/internal/'+dataGroup
	head = {'Content-Type':'application/json'} # Encabezado necesario para la peticion
	# Este doble paso lo tuve que hacer para que me armara correctamente el JSON.
	# JSON necesita que sea con comillas "dobles", y las listas de python utilizan comillas 'simples'
	# This steps sanitizes the JSON records, due to JSON demanding "double quotes"
	# and Python lists using 'simple quotes'
	records_json = {"records":records}
	records_json = json.dumps(records_json)
	r = requests.patch(requestPath,records_json,verify=verify,auth=(user, passwd),headers=head)
	return r