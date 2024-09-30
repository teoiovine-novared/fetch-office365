import fetchIP
import sys
import argparse

if __name__ == "__main__":
	# Argumentos de llamada
	# Call arguments
	parser = argparse.ArgumentParser(description='Import and update F5 data group with MS 365 IP addresses \r Importa y actualiza un data group en F5 con IPs de MS 365')
	parser.add_argument('-i', '--ip',default="127.0.0.1",type=str,
					 	help="F5 IP")
	parser.add_argument('-d', '--datagroup',default="O365_list",type=str,
					 	help="Data group name - must exist")
	parser.add_argument('-u', '--user',default="admin",type=str,
					 	help="User with access to API")
	parser.add_argument('-p', '--passwd',default="default",type=str,
					 	help="User password")
	parser.add_argument('-k', '--unsecure',action='store_false',
					 	help="Do not verify SSL")
	parser.add_argument('-D', '--debug',action='store_true',
					 	help="Show verbose output")#TODO Debug statements
	args = parser.parse_args()
	print(args.ip)

	# Chequeamos la ultima version registrada por la app
	# Check the latest version recorded by the app
	latestVersion = 0 # 0 if first time the program runs. 0 si es la primera vez que corre.
	version_file = open("latest_version", "r")
	latestVersion = int(version_file.read())
	version_file.close()
	o365Version = int(fetchIP.checkVersion())

	if o365Version > latestVersion:
		# Construimos una lista con registros unicos de las IPv4 e IPv6.
		# Descartamos URLS.
		# TODO: Agregar soporte para URLS.
		# Build a list with unique IPv4 and IPv6 addresses.
		# Discards URLS.
		# TODO: Support for URLS.
		o365List_raw = fetchIP.getIps()
		o365List_unique = []
		for x in o365List_raw:
			# No todos los id tienen IP. Si lo mostras asi nomas, te da error.
			# Por eso chequeamos si existe primero
			# Not every id has IP addresses in them.
			# Could run in some errors if we don't verify.
			if "ips" in x:
				for y in x['ips']:
					if y not in o365List_unique:
						o365List_unique.append(y)
		# Enviamos la lista al F5
		# Send list to F5
		r = fetchIP.patchDataGroup(args,o365List_unique)
		# Devolvemos el codigo de respuesta a logger
		# Return response code to logger
		if r:
			print(r.status_code,r.reason+" Success!!")
			version_file = open("latest_version", "w")
			version_file.write(str(o365Version))
			version_file.close()
	else:
		# Should modify this to your language or message of preference
		sys.stdout.write("No need to update. Latest version: " + str(o365Version))
