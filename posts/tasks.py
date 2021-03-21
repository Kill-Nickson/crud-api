from crud_api.celery import app
from .models import Post


@app.task
def reset_all_upvotes():
    Post.amount_of_upvotes.through.objects.all().delete()
    print("Posts have been successfully reset!")
