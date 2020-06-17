import requests
import time
import random

t = 1
color_array = []
blue_score = 0
red_score = 0
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'
link_touchtile =  'http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles'




def background(colortuple):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + colortuple[0] + " " + colortuple[1] + " " + colortuple[2] + " 0 200"
    color_array.append(toAppend)

def background2(colortuple):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + colortuple[0] + " " + colortuple[1] + " " + colortuple[2] + " 0 200"
    color_array[id] = toAppend

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

def spawn_moles(colortuple, existing):
  new_mole = random.randint(13, 101)
  color_data_new_mole = str(new_mole) + " " + "1 " + colortuple[0] + " " + colortuple[1] + " " + colortuple[2] + " 0 200"
  color_array[new_mole] = color_data_new_mole
  print(color_data_new_mole)
  existing.append(str(new_mole))
  Send_module(color_array)

def delete_mole(colortuple, id):
  color_data_new_mole = str(id) + " " + "1 " + colortuple[0] + " " + colortuple[1] + " " + colortuple[2] + " 0 200"
  color_array[int(id)] = color_data_new_mole
  Send_module(color_array)

def row_lines(begin_row, r, g, b):
  for column in range(6):
    begin_line = int(begin_row) + (1 * int(column))
    color_data1 = str(begin_line) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[begin_line] = color_data1
    print(color_array)
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
      print(input[num], every)
      if input[num] == every:
        equal.append(every)
  return equal

def scoreboard(scorepone, scoreptwo, we_have_a_winner, orginalColor, pone, ptwo):
  total = scorepone + scoreptwo
  percentagepone = (scorepone/total) * 100
  percentageptwo = (scoreptwo/total) * 100
  if 45 <= percentagepone <= 55 and 45 <= percentageptwo <= 55:
    color_data1 = str(1) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[0] = color_data1
    color_data1 = str(2) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[1] = color_data1
    color_data1 = str(3) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[2] = color_data1
    color_data1 = str(4) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[3] = color_data1
    color_data1 = str(5) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[4] = color_data1
    color_data1 = str(6) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[5] = color_data1
  if 40 <= percentagepone <= 44:
    color_data1 = str(1) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[0] = color_data1
    color_data1 = str(2) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[1] = color_data1
    color_data1 = str(3) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[2] = color_data1
    color_data1 = str(4) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[3] = color_data1
    color_data1 = str(5) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[4] = color_data1
    color_data1 = str(6) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[5] = color_data1
  if 37 <= percentagepone <= 39:
    color_data1 = str(1) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[0] = color_data1
    color_data1 = str(2) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[1] = color_data1
    color_data1 = str(3) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[2] = color_data1
    color_data1 = str(4) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[3] = color_data1
    color_data1 = str(5) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[4] = color_data1
    color_data1 = str(6) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[5] = color_data1
  if 36 > percentagepone:
    we_have_a_winner = True
    print("gewonnen2")
    background2(pone)
    time.sleep(0.2)
    pass
  if 40 <= percentageptwo <= 44:
    color_data1 = str(1) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[0] = color_data1
    color_data1 = str(2) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[1] = color_data1
    color_data1 = str(3) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[2] = color_data1
    color_data1 = str(4) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[3] = color_data1
    color_data1 = str(5) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[4] = color_data1
    color_data1 = str(6) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[5] = color_data1
  if 37 <= percentageptwo <= 39:
    color_data1 = str(1) + " " + "1 " + "255" + " " + "0" + " " + "0" + " 0 200"
    color_array[0] = color_data1
    color_data1 = str(2) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[1] = color_data1
    color_data1 = str(3) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[2] = color_data1
    color_data1 = str(4) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[3] = color_data1
    color_data1 = str(5) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[4] = color_data1
    color_data1 = str(6) + " " + "1 " + "0" + " " + "0" + " " + "250" + " 0 200"
    color_array[5] = color_data1
  if 36 > percentageptwo:
    we_have_a_winner = True
    print("gewonnen2")
    background2(ptwo)
    time.sleep(0.2)
    pass
  Send_module(color_array)


def main():
  ptwo = ("240", "0", "0")
  pone = ("0", "0", "240") 
  orginalColor = ("122", "130", "59")
  total_pone_spawns = 0
  total_ptwo_spawns = 0
  we_have_a_winner = False
  background(orginalColor)
  Send_module(color_array)
  existingpone = []
  existingptwo = []
  scorepone = 5
  scoreptwo = 5
  row_lines(7, "20", "20", "170")
  while we_have_a_winner == False:
    scoreboard(scorepone, scoreptwo, we_have_a_winner, orginalColor, ptwo, pone)
    while total_pone_spawns < 3:
     spawn_moles(pone, existingpone)
     total_pone_spawns += 1
    while total_ptwo_spawns < 3:
     spawn_moles(ptwo, existingptwo)
     total_ptwo_spawns += 1
    print(existingpone, existingptwo)
    touchInput = init_touchtext(tilelistener())
    RightOneTouchedPone = touchComparison(existingpone, touchInput)
    RightOneTouchedPtwo = touchComparison(existingptwo, touchInput)
    if len(RightOneTouchedPone) > 0:
      existingpone.remove(RightOneTouchedPone[0])
      delete_mole(orginalColor, RightOneTouchedPone[0])
      total_pone_spawns = total_pone_spawns - 1
      scorepone = scorepone + 1
      continue
    if len(RightOneTouchedPtwo) > 0:
      existingptwo.remove(RightOneTouchedPtwo[0])
      delete_mole(orginalColor, RightOneTouchedPtwo[0])
      total_ptwo_spawns = total_ptwo_spawns - 1
      scoreptwo = scoreptwo + 1
      continue
    else:
      print("doe niks")
  # background2(orginalColor)




main()