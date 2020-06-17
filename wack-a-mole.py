import requests
import time
import random

t = 1
color_array = []
blue_score = 0
red_score = 0
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'
link_touchtile =  'http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles'
existing = []



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

  #clicked panels ophalen
  x = requests.get('http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles')
  test = x.text
  print("clicked panel is")

  #  blue mol clickbaar maken
  print(test)
  print("Blue mole is")
  print(blue_mole)

  if str(blue_mole) in test:
    clicked_mole = int(blue_mole)
    color_data_bg = str(clicked_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[clicked_mole] = color_data_bg
    # blue_score bijhouden
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
    # red_score bijhouden
    red_score =+ 1
    print("red score is")
    print(red_score)
  else:
    color_data_red_mole = str(red_mole) + " " + "1 " + br + " " + bg + " " + bb + " 0 200"
    color_array[red_mole] = color_data_red_mole
  
    # score board laten zien 
    
  Send_module(color_array)

def spawn_moles(r, b, g, existing):
  new_mole = random.randint(13, 101)
  color_data_new_mole = str(new_mole) + " " + "1 " + r + " " + g + " " + b + " 0 200"
  color_array[new_mole] = color_data_new_mole
  print(color_data_new_mole)
  existing.append(new_mole)
  Send_module(color_array)




# Opens a stream that takes all touch input
def tilelistener():
  touchtile = requests.get(link_touchtile)
  # print(1)
  status_code = 200
  if touchtile.status_code == 200:
    touchdata = touchtile.text
    # print(2)
  else:
    status_code = 100
    while status_code != 200:
      touchtile = requests.get(link_touchtile)
      # print(3)
      if touchtile.status_code == 200:
        status_code = 200
        # print(4)
        touchdata = touchtile.text
        # print(5)
  return touchdata

# Proces the touchdata to compare it later in a function
def init_touchtext(string):
  newstring = string.replace("{\"events\":[{","").replace("}]}","")
  # print(newstring)
  array = newstring.split(",")
  datarray = []
  for every in array:
    if every.find("\"panelId\"") != -1:
      newevery = every.replace("\"", "").replace("panelId:", "")
      datarray.append(newevery)
  return datarray

# Compare if the right tile is clicked
def touchComparison(wanted, input):
  equal = []
  for every in wanted:
    for num in range(len(input)):
      if input[num] == every:
        equal.append(every)
  return equal

def main():
  poner = "240"
  poneg = "200"
  poneb = "100"
  ptwor = "240"
  ptwog = "200"
  ptwob = "100"
  total_pone_spawns = 0
  total_ptwo_spawns = 0
  we_have_a_winner = False
  background("122", "130", "59")
  Send_module(color_array)
  while we_have_a_winner == False:
    if total_pone_spawns < 3:
     spawn_moles(poner, poneg, poneb, existing)
     print(total_pone_spawns)
     total_pone_spawns += 1
    if total_ptwo_spawns < 3:
     spawn_moles(ptwor, ptwog, ptwob, existing)
     total_ptwo_spawns += 1
    print(existing)
    for spawn in existing:
      print(init_touchtext(tilelistener()))
      touchInput = init_touchtext(tilelistener())
      RightOneTouchedP = touchComparison(existing, touchInput)
      print(1)
      if len(RightOneTouchedP) > 0:
        existing.remove(existing)
        print(5)




main()