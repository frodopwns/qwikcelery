from celery import Celery

app = Celery(
    'myapp',
    broker='amqp://guest@localhost//',
    backend='redis',
)

@app.task
def add(x, y):
    return x + y

@app.task
def mult(x, y):
    return x * y

if __name__ == '__main__':
    app.start()
