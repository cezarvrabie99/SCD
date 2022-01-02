from celery import Celery

app = Celery('celery_task_add', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
