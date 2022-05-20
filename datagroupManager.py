import fetchIP
import sys

# Defaults para los argumentos de llamada
# Los usamos ahora para testear tranquilos

f5Host = "10.100.107.32" # IP por defecto del F5 si no dan uno por argumento (TODO: 127.0.0.1)
dataGroupName = "O365_list" # Nombre por defecto del datagroup si no dan uno por argumento
latestVersion = 64343653465436 # Ultima version registrada. La ponemos en 0 si el programa comienza por primera vez (pongo en 0 para forzar)
user = "admin" # (Para test, esto debería venir siempre por argumento)
passwd = "123momia" # (idem)
verify = bool(0)

# Argumentos de llamada
# TODO: Hacer que no importe el orden

#f5Host = str(sys.argv[1])
#dataGroupName = str(sys.argv[2])
#latestVersion = int(sys.argv[3])
#user = str(sys.argv[4])
#passwd = str(sys.argv[5])
#verify = bool(sys.argv[6])

o365Version = int(fetchIP.checkVersion())

if o365Version > latestVersion:
	o365List_raw = fetchIP.getIps()
	o365List_unique = []
	for x in o365List_raw:
		# No todos los id tienen IP. Si lo mostras asi nomas, te da error.
		# Por eso chequeamos si existe primero
		if "ips" in x:
			for y in x['ips']:
				if y not in o365List_unique:
					# Solo agrego a la lista los valores que no están ya en ella
					o365List_unique.append(y)
	# Enviamos la lista al F5
	r = fetchIP.patchDataGroup(f5Host,dataGroupName,user,passwd,verify,o365List_unique)
	# Devolvemos el codigo de respuesta del F5
	print(r.status_code,r.reason)
else:
	sys.stdout.write("No es necesario actualizar. Ultima version: " + str(o365Version))