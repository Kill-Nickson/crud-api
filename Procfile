release: python manage.py migrate

web: gunicorn crud_api.wsgi --log-file -

worker: celery -A crud_api worker -l info

worker2: celery -A crud_api beat -l info