import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
  hostname = socket.gethostname()
  ip = socket.gethostbyname(hostname)
  return 'La IP interna de esta maquina es {}.\n'.format(ip)

app.run(host='0.0.0.0', port=80)
