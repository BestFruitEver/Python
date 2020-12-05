from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Bonjour {nom} !</h3>" \
           "<b>Hostname:</b> {hostname}" 
    return html.format(nom=os.getenv("NOM","H3HITEMA"), hostname=socket.gethostname())

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)