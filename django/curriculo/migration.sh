#!/bin/bash

#Script responsável pelas migrations utilizadas pelo django.

python3 manage.py makemigrations api_curriculo
sleep 2
python3 manage.py migrate
sleep 2
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin_password')" | python3 manage.py shell
