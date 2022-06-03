#!/bin/bash
# Script para el crontab. Simplemente se trae las variables del otro archivo y
# se las pasa al script de Python
# TODO: hacer que modifique el parameters.sh con la version de O365 si hace falta

cd /home/admin/fetch-office365 # Ver como no hardcodear esto
source parameters.sh
logger -s "============================="
logger -s "Ejecutando o365_list_update.sh"
logger -s "Resultado:" ; python dataGroupManager.py $IP $NAME $USER $PASS $SSL | logger
logger -s "Fin de ejecucion"
logger -s "============================="
