from flask import Flask, render_template, request
from time import time, sleep
import random
import json
app = Flask(__name__,template_folder='template')

Numbers = [["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"], 
["18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34"],
["35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51"],
["52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68"],
["69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85"],
["86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102"]]


<<<<<<< HEAD
@app.route('/', methods=["GET"])
def index():
    # i = 0
    # while (i < 90):
    #     sleep(1)
    #     i += 1
    
    
    return render_template("Test.html", len = 17, Numbers = Numbers)
=======
def randomMole():
    j = "0"
    for D in range(0, 17):
        for k in Numbers:
            j = random.choice(k)
    
    return j
randomMole()

@app.route('/', methods=["GET"])
def index():
    i = 0
    while (i < 90):
        sleep(1)
        j = randomMole()
        i += 1
        
    return render_template("Test.html", len = 17, Numbers = Numbers, j = j)
>>>>>>> 9fcfdd33f0165fd9c1699ccb25174b942786e68f


if __name__== "__main__":
   app.run(debug=True)