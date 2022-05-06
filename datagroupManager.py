import fetchIP
import sys

# Argumentos de llamada
# TODO: Hacer que no importe el orden

f5Host = str(sys.argv[1])
dataGroupName = str(sys.argv[2])
latestVersion = int(sys.argv[3])
user = str(sys.argv[4])
passwd = str(sys.argv[5])
verify = bool(sys.argv[6])

o365Version = int(fetchIP.checkVersion())

if o365Version > latestVersion:
	o365List = fetchIP.getIps()
	dataGroup = fetchIP.getDataGroup(f5Host,dataGroupName,user,passwd,verify)
	# TODO: Pensar como actualizar el datagroup.
	# Hay que poner un chequeo para ver si existe en primera instancia
	# Una vez que está creado, borrarlo y crearlo de nuevo si hay updates no me parece una opcion
	# Si el volumen de traifoc es muy grande, ese interim, aunque breve, puede generar errores.
	# Lo ideal sería chequear la diferencia. ¿Cómo? 
	for x in dataGroup['records']:
		print(x['name'])
	for x in o365List:
		# No todos los id tienen IP. Si lo mostras asi nomas, te da error.
		# Por eso chequeamos si existe primero
		if "ips" in x:
			pass
			#print(x['ips'])
else:
	print("Tenemos la ultima version")