from nanoleafapi import discovery, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, LIGHT_BLUE, PINK, PURPLE, WHITE
from flask import Flask

app = Flask(__name__)

auth_token = "yD3RlM2LKIBAUJXxILjnjeBIKtxLGroB"
ip = "192.168.3.34"

nl = Nanoleaf(ip, auth_token)

#nl.set_color(PURPLE)
#nl.set_color((210,105,30))

x = nl.list_effects()
print (x)

effects = ['Color Burst', 'Falling Whites', 'Fireworks', 'Flames', 'Forest', 'Inner Peace', 'Meteor Shower', 'Nemo', 'Northern Lights', 'Paint Splatter', 'Pulse PopBeats', 'Radial Sound Bar', 'Rhythmic Northern Lights', 'Romantic', 'Sound Bar', 'Streaking Notes']
 
nl.set_effect(effects[0])

y = nl.get_current_effect()
print (y)