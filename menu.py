# imports
import requests
import time
import random

# global variables
t = .5
color_array = []
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'
link_touchtile =  'http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles'

# Function to define to whole colorstring, always start whit this function
def background(r, g, b):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array.append(toAppend)
  return "done"

# Function defines a new one-color-background, when there is already an background
def background2(r, g, b):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[id] = toAppend
    for row in range(17):
      idnum = 6 * row
      if id == idnum:
        time.sleep(0.1)
        Send_module(color_array)
  return "done"

# Makes it easy to send the colordata to mocking server
def Send_module(color_array):
  colorstring = "102"
  for id in color_array:
    colorstring += " " + id
  myobj = {"command": "display",
  "animType": "static",
  "animData": colorstring,
  "loop": False}
  requests.post(link_colorstring, data = myobj)


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

# defined a specific view of the menu, frame to select the number of players
def game_select_view1():
  toAppend = str(62) + " " + "1 " + "255" + " " + "16" + " " + "16" + " 0 200"
  color_array[62] = toAppend
  Send_module(color_array)
  time.sleep(0.2)
  toAppend = str(65) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  color_array[65] = toAppend
  Send_module(color_array)
  time.sleep(0.2)
  toAppend = str(80) + " " + "1 " + "245" + " " + "223" + " " + "26" + " 0 200"
  color_array[80] = toAppend
  Send_module(color_array)
  time.sleep(0.2)
  toAppend = str(83) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[83] = toAppend
  Send_module(color_array)
  return "done"

# defined a specific view of the menu, frame to select the number of players
def player_count_select_view1():
  toAppend = str(15) + " " + "1 " + "245" + " " + "223" + " " + "26" + " 0 200"
  color_array[15] = toAppend
  toAppend = str(33) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  color_array[33] = toAppend
  toAppend = str(40) + " " + "1 " + "6" + " " + "97" + " " + "255" + " 0 200"
  color_array[40] = toAppend
  toAppend = str(58) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[58] = toAppend
  toAppend = str(63) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[63] = toAppend
  toAppend = str(70) + " " + "1 " + "64" + " " + "162" + " " + "67" + " 0 200"
  color_array[70] = toAppend
  Send_module(color_array)
  return "done"

# A function used to find the border
def search_for_nearest_value(value, list, direction):
  if direction == "Up":
    nearest_number_found = False
    while nearest_number_found == False:
      value_exist = list.count(value)
      if value_exist == 1:
        return value
      value += 1
  if direction == "Down":
    nearest_number_found = False
    while nearest_number_found == False:
      value_exist = list.count(value)
      if value_exist == 1:
        return value
      value = value - 1

# a function that makes it easy to find a column number by giving the tileID
def find_column_number(tileID):
  found = False
  UpBorderTile2 = [1, 2, 3, 4, 5, 6]
  while found == False:
    if UpBorderTile2.count(tileID) == 1:
      return tileID
    else:
      tileID -= 6

#a addation to make it more beautifull
def radialWaveAnimation(midTile, MainColorRed, MainColorGreen, MainColorBlue, AccentColorRed, AccentColorGreen, AccentColorBlue):
  # variables
  tilesTilLeftEnd = []
  tilesTilRightEnd = []
  tilesTilUpEnd = []
  tilesTilDownEnd = []
  LeftBorderTile = []
  RightBorderTile = []
  UpBorderTile = [1]
  DownBorderTile = [97]
  length_of_to_Left_list = 0
  length_of_to_Right_list = 0
  length_of_to_Up_list = 0
  length_of_to_Down_list = 0
  # calculate wich tiles
  for num in range(17):
    tile = 1 + 6 * num
    LeftBorderTile.append(tile)
  for num in range(17):
    tile = 6 + 6 * num
    RightBorderTile.append(tile)
  tile = 1
  for num in range(5):
    tile += 1
    UpBorderTile.append(tile)
  tile = 97
  for num in range(5):
    tile += 1
    DownBorderTile.append(tile)
  # tiles til Left
  border = search_for_nearest_value(midTile, LeftBorderTile, "Down")
  tilesTilLeftEnd = list(range(border, midTile))
  tilesTilLeftEnd.reverse()
  # tiles til Right
  border = search_for_nearest_value(midTile, RightBorderTile, "Up")
  tilesTilRightEnd = list(range((midTile + 1), (border + 1)))
  # tiles til Up
  tile = midTile
  column_number = find_column_number(midTile)
  while tile is not column_number:
    tile -= 6
    tilesTilUpEnd.append(tile)
  # tiles til down
  tile = midTile
  column_number = find_column_number(midTile) + 96
  while tile is not column_number:
    tile += 6
    tilesTilDownEnd.append(tile)
  # calc lengths
  length_of_to_Left_list = len(tilesTilLeftEnd)
  length_of_to_Right_list = len(tilesTilRightEnd)
  length_of_to_Up_list = len(tilesTilUpEnd)
  length_of_to_Down_list = len(tilesTilDownEnd)
  # run program
  first_part_of_animation_busy = True
  loop_number = 0
  while first_part_of_animation_busy:
    print(tilesTilLeftEnd)
    print(length_of_to_Left_list)
    print(loop_number)
    if length_of_to_Left_list > (loop_number):
      tileID = tilesTilLeftEnd[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Right_list > (loop_number):
      tileID = tilesTilRightEnd[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Up_list > (loop_number):
      tileID = tilesTilUpEnd[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Down_list > loop_number:
      tileID = tilesTilDownEnd[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Left_list < (loop_number) and length_of_to_Right_list < (loop_number) and length_of_to_Up_list < (loop_number) and length_of_to_Down_list < loop_number:
      first_part_of_animation_busy = False
    loop_number += 1
    Send_module(color_array)
  
#the main code, it runs automaticly, this indentation level is made to shorten the code. When you're coding in this file you could hide this part.
def main():
  background("230", "230", "200")
  Send_module(color_array)
  player_count_select_view1()
  touchedTheWriteOne = False
  while touchedTheWriteOne == False:
    touchInput = init_touchtext(tilelistener())
    RightOneTouchedP = touchComparison(['15', '33', '40', '58', '63', '70'], touchInput)
    if len(RightOneTouchedP) > 0:
      touchedTheWriteOne = True
  time.sleep(0.5)
  background2("230", "200", "200")
  time.sleep(0.2)
  game_select_view1()
  touchedTheWriteOne = False
  while touchedTheWriteOne == False:
    touchInput = init_touchtext(tilelistener())
    RightOneTouchedG = touchComparison(['62', '65', '80', '83'], touchInput)
    if len(RightOneTouchedG) > 0:
      touchedTheWriteOne = True
  # if RightOneTouchedG == ['62']:
  #   print("62")
  # if RightOneTouchedG == ['65']:
  #   print("65")
  # if RightOneTouchedG == ['80']:
  #   print("80")
  # if RightOneTouchedG == ['83']:
  #   print("83")
  radialWaveAnimation(int(RightOneTouchedG[0]), "1", "1", "1", "1", "1", "1")

main()






