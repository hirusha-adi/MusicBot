import platform
import os
try:
    from flask import Flask
except:
    if platform.system().lower().startswith('win'):
        os.system("pip3 install flask")
    else:
        os.system("pip install flask")
    from flask import Flask

from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Hello, MusicBot is alive!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
