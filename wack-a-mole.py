import requests
import time
import random

t = 1
color_array = []
blue_score = 0
red_score = 0
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'


def background(r, g, b):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array.append(toAppend)

def Send_module(color_array):
  colorstring = "102"
  for id in color_array:
    colorstring += " " + id
  myobj = {"command": "display",
  "animType": "static",
  "animData": colorstring,
  "loop": False}
  requests.post(link_colorstring, data = myobj)


def Generate_mole(r, g, b , pr, pg, pb , br, bg, bb):

  blue_mole = random.randint(25, 101)
  red_mole = random.randint(25, 101)

  color_data_blue_mole = str(blue_mole) + " " + "1 " + r + " " + g + " " + b + " 0 200"
  color_array[blue_mole] = color_data_blue_mole
  
  color_data_red_mole = str(red_mole) + " " + "1 " + pr + " " + pg + " " + pb + " 0 200"
  color_array[red_mole] = color_data_red_mole

  Send_module(color_array)

  time.sleep(t)

  #  blue mol clickbaar maken
  x = requests.get('http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles')
  test = x.text
  print("clicked panel is")
  print(test)
  print("Blue mole is")
  print(blue_mole)
  if str(blue_mole) in test:
    clicked_mole = int(blue_mole)
    color_data_bg = str(clicked_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[clicked_mole] = color_data_bg
    # score bijhouden
    blue_score =+ 1
    print("blue score is")
    print(blue_score)
  else:
    color_data_blue_mole = str(blue_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[blue_mole] = color_data_blue_mole
  
  #  red mol clickbaar maken
  print("Red mole is")
  print(red_mole)
  if str(red_mole) in test:
    clicked_mole = int(red_mole)
    color_data_bg = str(clicked_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[clicked_mole] = color_data_bg
    # score bijhouden
    red_score =+ 1
    print("red score is")
    print(red_score)
  else:
    color_data_red_mole = str(red_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[red_mole] = color_data_red_mole
  
    # score board laten zien 
    
  Send_module(color_array)
  
  


background("122", "130", "59")
Send_module(color_array)
for x in range(60):
  Generate_mole("0", "0", "255", "255", "0", "0", "122", "130", "59")
