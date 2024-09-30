# fetch-office365
## (English) Introduction
Python/BASH script that pulls O365 IP list from Microsoft web service (https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide) and updates a data group in F5 to be used by an iRule or policy.

## How to use
1. Download the content of this repo.
2. Upload it to the F5 device, to a directory of your choice. We'll use /shared.
3. Modify parameters.sh as you need. Note that "NAME" should match the datagroup you'll create later
4. Assign execution permissions:
   - chmod +x -R /shared/fetch-office365/
   - chmod +rw /shared/fetch-office365/latest_version
   - chmod 700 /shared/fetch-office365/parameters.sh (this is important since it has a password)
   - If using another user to run the crontab: chown <user> /shared/fetch-office365/parameters.sh
5. Add directory to PATH:
   - Temporal: > export PATH="/shared/fetch-office365:$PATH"
   - Permanent: add 'export PATH="/shared/fetch-office365:$PATH"' at the end of .bashrc
6. Modify o365_list_update.sh and dataGroupManager.py since log messages are written in spanish.
7. Add o365_list_update.sh to crontab:
   - 0 1 28 * * o365_list_update.sh > /var/tmp/cronjob.log 2>&1
   - Since O365 list is rarely updated, we set it to run once a month
   - Then it prints output to /var/tmp/cronjob.log so we know it ran.
8. Create an empty datagroup.
   - Can be named as you wish, just be sure you set it so in parameters.sh
9. Run the script for the firs time with ./o365_list_update.sh

Done! Now you can use your datagroup in an iRule with 
> class match IP equals "O365_list"

## (Español) Introducción
Script en Python/BASH que trae la lista de IPs de O365 desde su servicio web (https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide) y actualiza un data group en F5 para ser usado por una iRule o política.

## Cómo usar
1. Descargar el contenido de este repo.
2. Subirlo a un directorio en el F5. Nosotros usamos /shared.
3. Modificar paramters.sh con los datos necesarios. Cuidado con "NAME" que debe coincidir con el datagroup del paso 8.
4. Asignar permisos:
   - chmod +x -R /shared/fetch-office365/
   - chmod +rw /shared/fetch-office365/latest_version
   - chmod 700 /shared/fetch-office365/parameters.sh (importante porque hay contraseñas)
   - Si se utiliza otro usuario para correr el script: chown <user> /shared/fetch-office365/parameters.sh
5. Añadir el directorio a PATH:
   - Temporal: > export PATH="/shared/fetch-office365:$PATH"
   - Permanente: add 'export PATH="/shared/fetch-office365:$PATH"' al final de .bashrc
6. Agregar o365_list_update.sh a crontab:
   - 0 1 28 * * o365_list_update.sh > /var/tmp/cronjob.log 2>&1
   - Ya que O365 se actualiza poco frecuentemente, lo configuramos para que se ejecute una vez al mes.
   - Luego imprime el resultado a cronjob.log para corroborar el resultado.
7. Crear un datagroup vacío.
   - El nombre es indistinto, solo debe coincidir con el seteado en parameters.sh
8. Correr el script por primera vez con ./o365_list_update.sh

¡Listo! Ahora podés usar el datagroup en una iRule con
> class match IP equals "O365_list"



