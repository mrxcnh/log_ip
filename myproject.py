import socket
import platform
from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    print(f"{request.remote_addr}")
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')

