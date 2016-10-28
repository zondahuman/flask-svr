# -*- coding:utf-8 -*-
from flask import Flask,render_template

app = Flask(__name__)

#route() 装饰器把一个函数绑定到对应的 URL 上。
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
