#!/bin/bash
# Script para el crontab. Simplemente se trae las variables del otro archivo y
# se las pasa al script de Python
# TODO: hacer que modifique el parameters.sh con la version de O365 si hace falta

source parameters.sh
python3.8 dataGroupManager.py $IP $NAME $VERSION $USER $PASS $SSL