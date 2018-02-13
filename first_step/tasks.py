from celery import Celery

# backend_string = 'db+postgresql://slow999:lyq999@localhost/mycelery'
app = Celery('tasks',
             backend='rpc://',
             broker='pyamqp://guest@localhost//'
     )
# app.conf.task_serializer = 'json'
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y
