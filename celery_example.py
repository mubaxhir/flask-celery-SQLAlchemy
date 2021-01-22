from flask import Flask
from tasks import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] ='amqp://localhost//'
app.config['CELERU_BACKEND'] = 'db+sqlite:///celery.sqlite'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///celery.sqlite'
db = SQLAlchemy(app)
celery = make_celery(app)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I have sent it to backend'

@celery.task(name='task.reverse')
def reverse(text):
    return text[::-1]

@app.route('/insertdata')
def insertdata():
    insert.delay()
    return "async request is sent"

@celery.task(name='celery_example.insert')
def insert():
    for i in range(500):
        data = ''.join(choice('ABCDE') for i in range(10))
        db.session.add(Results(data=data))
    db.session.commit()
    return "Done!!"

if __name__ == '__main__':
    app.run(debug=True,port=4444)