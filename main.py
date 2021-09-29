from flask import Flask

app = Flask(__name__)


@app.route('/aws_flask_app', methods=['GET'])
def aws_flask_app(aws_flask_app):
    return "AWS_FLASK_APP!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
