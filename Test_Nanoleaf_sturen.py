from flask import Flask, jsonify, request
from flask_cors import CORS
from nanoleafapi import discovery, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, LIGHT_BLUE, PINK, PURPLE, WHITE
# import nanoleafdb

auth_token = "yD3RlM2LKIBAUJXxILjnjeBIKtxLGroB"
ip = "192.168.3.34"
nl = Nanoleaf(ip, auth_token)



effect = nl.list_effects()
app = Flask(__name__, static_folder='static', static_url_path='')

CORS(app)

@app.route('/effecten', methods = ['GET']) 
def EffectOption():
    # print("hallo")
    # print(request.json)
    # effects = request.json
    # nl.set_effects()
    # app.logger.debug(jsonify(effect))
    return (jsonify(effect))

# # nl.set_color(PURPLE)
# nl.set_color((210,105,30))

# effects = ['Color Burst', 'Falling Whites', 'Fireworks', 'Flames', 'Forest', 'Inner Peace', 'Meteor Shower', 'Nemo', 'Northern Lights', 'Paint Splatter', 'Pulse PopBeats', 'Radial Sound Bar', 'Rhythmic Northern Lights', 'Romantic', 'Sound Bar', 'Streaking Notes']

# nl.set_effect(effects[4])

# from nanoleafapi import Nanoleaf
# from flask import Flask

# ip = "192.168.3.34"
# auth_token = "yD3RlM2LKIBAUJXxILjnjeBIKtxLGroB"
# nl = Nanoleaf(ip, auth_token)

# app = Flask(__name__)

# @app.route('/send_effect/', methods = ['PUT'])
# def effect():
# nl.list_effects()
# print(nl.list_effects())
    # return (nl.list_effects(), 200)

# app.run(debug=True)


@app.route('/effect', methods = ['PUT'])
def effects():
    effect1 = request.get_json()['effect']
    nl.set_effect(effect1)
    # app.logger.debug(jsonify(effect))
    return ()


app.run(debug=True)