import fetchIP
# TODO: Esto esta mal. latestVersion tiene que quedar guardado en un archivo
# y bash tiene que ejecutar este script como main y enviar esa version como argumento.
# En el script de iRuleLX se podía obviar porque quedaba guardado en memoria.
# Pero no queremos hacer eso

o365Version = fetchIP.checkVersion()

try:
	if o365Version > latestVersion:
		latestVersion = o365Version
		print("1")
	else:
		print("2")
except NameError:
	latestVersion = o365Version
	print("3")
except:
	print("4")

#if "latestVersion" in locals() or 
#	for x in o365List:
# 		No todos los id tienen IP. Si lo mostras asi nomas, te da error.
# 		Por eso chequeamos si existe primero
#		if "ips" in x:
#			print(x['ips'])
#else:
#	pass
