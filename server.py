import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def get_heartrate():
    r = requests.get(url="https://api.particle.io/v1/devices/events?access_token=429c3f0a74c0602736cde1e56cac6a54d1fc8765")
    return str(r.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
