import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crud_api.settings")

app = Celery("crud_api")

app.conf.update(
    BROKER_URL="redis://:oEWaYhs7sMC6cP0yC4G40ro9CF5yMTix@redis-18285.c78.eu-"
               "west-1-2.ec2.cloud.redislabs.com:18285",
    CELERY_RESULT_BACKEND="redis://:oEWaYhs7sMC6cP0yC4G40ro9CF5yMTix@redis-18"
                          "285.c78.eu-west-1-2.ec2.cloud."
    "redislabs.com:18285",
)

app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.beat_schedule = {
    "reset all upvotes everyday at 6 am": {
        "task": "posts.tasks.reset_all_upvotes",
        'schedule': crontab(hour=6),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
