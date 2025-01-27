import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                datetime.datetime.now().utcnow()

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/counter')
def counter():
    counter_value = int(app.config.get('COUNTER', 0))
    app.config['COUNTER'] = counter_value + 1
    return 'Счетчик: %s' % counter_value