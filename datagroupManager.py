import fetchIP
import sys

f5Host = "127.0.0.1" # Default IP
dataGroupName = "O365_list" # Default data group
latestVersion = 0 # 0 if first time the program runs. 0 si es la primera vez que corre.
user = "admin" # defaults to admin
verify = True # defaults to check ssl authenticity

# Argumentos de llamada
# Call arguments

f5Host = str(sys.argv[1])
dataGroupName = str(sys.argv[2])
user = str(sys.argv[3])
passwd = str(sys.argv[4])
verify = bool(int(sys.argv[5]))


# Chequeamos la ultima version registrada por la app
# Check the latest version recorded by the app
version_file = open("latest_version", "r")
latestVersion = int(version_file.read())
version_file.close()
o365Version = int(fetchIP.checkVersion())

if o365Version > latestVersion:
        # Construimos una lista con registros unicos de las IPv4 e IPv6.
        # Descartamos URLS.
        # TODO: Agregar soporte para URLS.
        # Build a list with unique IPv4 or IPv6 addresses.
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
        r = fetchIP.patchDataGroup(f5Host,dataGroupName,user,passwd,verify,o365List_unique)
        # Devolvemos el codigo de respuesta a logger
        # Return response code to logger
        print(r.status_code,r.reason)
        version_file = open("latest_version", "w")
        version_file.write(str(o365Version))
        version_file.close()
else:
        # Should modify this to your language or message of preference
        sys.stdout.write("No es necesario actualizar. Ultima version: " + str(o365Version))