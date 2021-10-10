#!/bin/bash
echo "A:"
python manage.py migrate
echo "B:"
echo $(pwd)
ls -al
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root@admin.com', '1234')"
echo "C:"
python manage.py runserver 0.0.0.0:8000