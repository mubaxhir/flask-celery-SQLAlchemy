from celery import Celery 

#     celery = Celery('tasks',broker='amqp://mubashir:panacloud@localhost:5672/myvhost',backend='db+sqlite')
def make_celery(app):
    celery = Celery('tasks',broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERU_BACKEND'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract=True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

