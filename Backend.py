from flask import Flask, jsonify, request
from flask_cors import CORS
from nanoleafapi import discovery, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, LIGHT_BLUE, PINK, PURPLE, WHITE

auth_token = "yD3RlM2LKIBAUJXxILjnjeBIKtxLGroB"
ip = "192.168.3.34"
nl = Nanoleaf(ip, auth_token)



effect = nl.list_effects()
app = Flask(__name__, static_folder='static', static_url_path='')

CORS(app)

@app.route('/effecten', methods = ['GET']) 
def EffectOption():
    
    return (jsonify(effect))


@app.route('/effect', methods = ['PUT'])
def effects():
    effect1 = request.get_json()['effect']
    nl.set_effect(effect1)

    return ()


app.run(debug=True)