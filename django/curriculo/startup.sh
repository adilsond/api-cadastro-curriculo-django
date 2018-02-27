#!/bin/bash
#10 segundos de sleep para que dê tempo para o servidor postgres inicializar.
sleep 10
if [ ! -f  "migrated.pid" ];
  then 
  /bin/bash migration.sh;
  touch migrated.pid;
fi
python3 manage.py runserver 0.0.0.0:8888
