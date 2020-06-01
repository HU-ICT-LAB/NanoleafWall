import requests
import time
import random

t = .5
color_array = []
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'
link_touchtile =  'http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles'

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

def tilelistener():
  touchtile = requests.get(link_touchtile)
  print(1)
  status_code = 200
  if touchtile.status_code == 200:
    touchdata = touchtile.text
    print(2)
  else:
    status_code = 100
    while status_code != 200:
      touchtile = requests.get(link_touchtile)
      print(3)
      if touchtile.status_code == 200:
        status_code = 200
        print(4)
        touchdata = touchtile.text
        print(5)
  return touchdata

def init_text(string):
  newstring = string.replace("{\"events\":[{","").replace("}]}","")
  print(newstring)
  array = newstring.split(",")
  datarray = []
  for every in array:
    if every.find("\"panelId\"") != -1:
      newevery = every.replace("\"", "").replace("panelId:", "")
      datarray.append(newevery)
      print(newevery)
  return datarray

def touchComparison(wanted, input):
  equal = []
  for every in wanted:
    for num in range((len(input) + 1)):
      print(every, num)
      if input[num] == every:
        equal.append(every)
  return equal

def game_select_view1():
  background("230", "230", "250")
  print(color_array)
  Send_module(color_array)
  toAppend = str(62) + " " + "1 " + "255" + " " + "16" + " " + "16" + " 0 200"
  color_array[62] = toAppend
  Send_module(color_array)
  toAppend = str(65) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  print(color_array)
  color_array[65] = toAppend
  Send_module(color_array)
  toAppend = str(80) + " " + "1 " + "245" + " " + "223" + " " + "26" + " 0 200"
  color_array[80] = toAppend
  Send_module(color_array)
  toAppend = str(83) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[83] = toAppend
  Send_module(color_array)

def player_count_select_view1():
  toAppend = str(15) + " " + "1 " + "245" + " " + "223" + " " + "26" + " 0 200"
  color_array[15] = toAppend
  Send_module(color_array)
  toAppend = str(33) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  color_array[33] = toAppend
  Send_module(color_array)
  toAppend = str(40) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  color_array[40] = toAppend
  Send_module(color_array)
  toAppend = str(58) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[58] = toAppend
  Send_module(color_array)
  toAppend = str(63) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[63] = toAppend
  Send_module(color_array)
  toAppend = str(70) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[70] = toAppend
  Send_module(color_array)
  

background("230", "230", "250")
Send_module(color_array)
player_count_select_view1()
time.sleep(10)
game_select_view1()
# print(touchComparison([3, 0, 2, 5, 70], init_text(tilelistener())))





