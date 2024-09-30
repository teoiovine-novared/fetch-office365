import uuid
import json
import requests # type: ignore
import sys



# Funcion para hacer los llamados a O365
# 	method= version: trae versiones; endpoints= trae urls/ips
# 	scope= Worldwide: todos. No vamos a usar otro, pero conviene dejarlo asi
# Helper function to build calls to O365
#	method= version pull versions; method= endpoints pulls urls/ips JSON
#	scope= Worlwide: everything. We do not use other than that.
def urlHelper(method,scope):
	ws = "https://endpoints.office.com"
	guid = str(uuid.uuid4())
	requestPath = ws+'/'+method+'/'+scope+'?ClientRequestId='+guid
	try:
		r = requests.get(requestPath).text
	except requests.exceptions.Timeout:
		sys.stdout.write("Timeout connecting to MS")
	except requests.exceptions.TooManyRedirects:
		sys.stdout.write("Too many redirects")
	except requests.exceptions.ConnectionError:
		sys.stdout.write("Connection error. DNS or TCP related")
	except requests.exceptions.RequestException as e:
		sys.stdout.write("Catastrophic error. Exiting")
		raise SystemExit(e)
	else:
		return r

# Funcion para obtener la ultima version del archivo JSON de MS
# Function to get latest version of the MS JSON File
def checkVersion():
	return json.loads(urlHelper("version","Worldwide"))['latest']

# Funcion para traernos las IP de O365
# Function to get O365 Ips
def getIps():
	return json.loads(urlHelper("endpoints","Worldwide"))

# Funcion para traer el data group entero del F5
# Era necesaria en otra version del script, pero ya no se utiliza
# La dejo por si en un futuro sirve
# Deprecated function to get whole data group from F5
# Leaving it just in case
def getDataGroup(args):
	requestPath = 'https://'+args.ip+'/mgmt/tm/ltm/data-group/internal/'+args.datagroup
	try:
		r = requests.get(requestPath,verify = args.unsecure,auth=(args.user, args.passwd)).text
		r.raise_for_status()
	except requests.exceptions.Timeout:
		sys.stdout.write("Timeout connecting to F5")
	except requests.exceptions.TooManyRedirects:
		sys.stdout.write("Too many redirects")
	except requests.exceptions.ConnectionError:
		sys.stdout.write("Connection error to F5. DNS or TCP related")
	except requests.exceptions.HTTPError:
		sys.stdout.write("HTTP Error getting DataGroup")
		sys.stdout.write(r.status_code+" "+r.reason)
	except requests.exceptions.RequestException as e:
		sys.stdout.write("Catastrophic error. Exiting")
		raise SystemExit(e)
	else:
		return json.loads(r)
# Funcion para subir el datagroup al F5
# Function to patch datagroup to F5
def patchDataGroup(args,records):
	requestPath = "https://"+args.ip+"/mgmt/tm/ltm/data-group/internal/"+args.datagroup
	head = {"Content-Type":"application/json"} # Encabezado necesario para la peticion
	# Este doble paso lo tuve que hacer para que me armara correctamente el JSON.
	# JSON necesita que sea con comillas "dobles", y las listas de python utilizan comillas "simples"
	# This steps sanitizes the JSON records, due to JSON demanding "double quotes"
	# and Python lists using "simple quotes"
	records_json = {"records":records}
	records_json = json.dumps(records_json)
	try:
		r = requests.patch(requestPath,records_json,verify=args.unsecure,auth=(args.user, args.passwd),headers=head)
		r.raise_for_status()
	except requests.exceptions.Timeout:
		sys.stdout.write("Timeout connecting to F5")
	except requests.exceptions.TooManyRedirects:
		sys.stdout.write("Too many redirects")
	except requests.exceptions.ConnectionError:
		sys.stdout.write("Connection error to F5. DNS, TCP or SSL related. Try -k?")
	except requests.exceptions.HTTPError:
		sys.stdout.write("HTTP Error patching DataGroup")
		sys.stdout.write(r.status_code+" "+r.reason)
	except requests.exceptions.RequestException as e:
		sys.stdout.write("Catastrophic error. Exiting")
		raise SystemExit(e)
	else:
		return r