from flask import Flask

app = Flask(__name__)


@app.route('/aws_flask_app/<name>', methods=['GET'])
def aws_flask_app(name):
    return "Hello, {}!, I'm the AWS_FLASK_APP!".format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
