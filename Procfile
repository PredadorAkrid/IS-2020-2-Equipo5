release: python manage.py makemigrations && manage.py migrate --noinput 
web: gunicorn nombre_del_proyecto.wsgi:application --log-file -