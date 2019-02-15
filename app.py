import os

from flask import Flask, jsonify
from flask_swagger import swagger
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask form alpine-linux!'


@app.route('/test')
def test():
    msg = """This is a test of the flask stystem on apline linux docker image!"""
    return jsonify(msg)


@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Test Flask App"
    return jsonify(swag)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
