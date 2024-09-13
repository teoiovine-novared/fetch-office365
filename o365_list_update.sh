#!/bin/bash
# Script para el crontab. Simplemente se trae las variables del otro archivo y
# se las pasa al script de Python
# "latest_version" puede ser eliminada, seria como eliminar cache.
# Script for crontab. Pulls variables from parameters.sh and calls python
# with parameters.
# "latest_version" file can be removed, works like clearing cache.


cd /home/admin/fetch-office365 # TODO: variable
source parameters.sh 
# Should change this messages to your preference
logger -s "============================="
logger -s "Ejecutando o365_list_update.sh"
logger -s "Resultado:" ; python dataGroupManager.py $IP $NAME $USER $PASS $SSL | logger
logger -s "Fin de ejecucion"
logger -s "============================="
