release: python manage.py migrate

web: gunicorn crud_api.wsgi --log-file - & celery -A crud_api worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo & celery -A crud_api beat -l info & wait -n
