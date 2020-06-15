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
    color_array[id - 1] = toAppend
    for row in range(17):
      idnum = 6 * row
      if id == idnum:
        time.sleep(0.1)
        Send_module(color_array)
  return "done"

def background3(r, g, b):
  for id in range(102):
    toAppend = str((id + 1)) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[id - 1] = toAppend
    for row in range(17):
      idnum = 6 * row
      if id == idnum:
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
  value = int(value)
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
  up_border_tile2 = [1, 2, 3, 4, 5, 6]
  while found == False:
    if up_border_tile2.count(tileID) == 1:
      return tileID
    else:
      tileID -= 6

def find_row_number(tileID):
  found = False
  row_number = 1
  up_border_tile2 = [1, 2, 3, 4, 5, 6]
  while found == False:
    if up_border_tile2.count(tileID) == 1:
      return row_number
    else:
      row_number += 1
      tileID -= 6

#a addation to make it more beautifull
def radial_Wave_Animation(midTile, MainColorRed, MainColorGreen, MainColorBlue, AccentColorRed, AccentColorGreen, AccentColorBlue):
  # variables
  tiles_Til_Left_End = []
  tiles_Til_Right_End = []
  tiles_Til_Up_End = []
  tiles_Til_Down_End = []
  Left_Border_Tile = []
  Right_Border_Tile = []
  Up_Border_Tile = [1]
  Down_Border_Tile = [97]
  length_of_to_Left_list = 0
  length_of_to_Right_list = 0
  length_of_to_Up_list = 0
  length_of_to_Down_list = 0
  # calculate wich tiles
  for num in range(17):
    tile = 1 + 6 * num
    Left_Border_Tile.append(tile)
  for num in range(17):
    tile = 6 + 6 * num
    Right_Border_Tile.append(tile)
  tile = 1
  for num in range(5):
    tile += 1
    Up_Border_Tile.append(tile)
  tile = 97
  for num in range(5):
    tile += 1
    Down_Border_Tile.append(tile)
  # tiles til Left
  border = search_for_nearest_value(midTile, Left_Border_Tile, "Down")
  tiles_Til_Left_End = list(range(border, midTile))
  tiles_Til_Left_End.reverse()
  # tiles til Right
  border = search_for_nearest_value(midTile, Right_Border_Tile, "Up")
  tiles_Til_Right_End = list(range((midTile + 1), (border + 1)))
  # tiles til Up
  tile = midTile
  column_number = find_column_number(midTile)
  while tile is not column_number:
    tile -= 6
    tiles_Til_Up_End.append(tile)
  # tiles til down
  tile = midTile
  column_number = find_column_number(midTile) + 96
  while tile is not column_number:
    tile += 6
    tiles_Til_Down_End.append(tile)
  # calc lengths
  length_of_to_Left_list = len(tiles_Til_Left_End)
  length_of_to_Right_list = len(tiles_Til_Right_End)
  length_of_to_Up_list = len(tiles_Til_Up_End)
  length_of_to_Down_list = len(tiles_Til_Down_End)
  # run program
  first_part_of_animation_busy = True
  loop_number = 0
  while first_part_of_animation_busy:
    print(tiles_Til_Left_End)
    print(length_of_to_Left_list)
    print(loop_number)
    if length_of_to_Left_list > (loop_number):
      tileID = tiles_Til_Left_End[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Right_list > (loop_number):
      tileID = tiles_Til_Right_End[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Up_list > (loop_number):
      tileID = tiles_Til_Up_End[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Down_list > loop_number:
      tileID = tiles_Til_Down_End[loop_number]
      toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
      color_array[tileID] = toAppend
    if length_of_to_Left_list < (loop_number) and length_of_to_Right_list < (loop_number) and length_of_to_Up_list < (loop_number) and length_of_to_Down_list < loop_number:
      first_part_of_animation_busy = False
    loop_number += 1
    Send_module(color_array)
  # ending anitmation
  animation_is_done = False
  animation_row_to_up = (find_row_number(midTile))
  animation_row_to_down = (find_row_number(midTile))
  print(animation_row_to_up)
  is_done = 0
  while animation_is_done == False:
    up_border_tile2 = [1, 2, 3, 4, 5, 6]
    if animation_row_to_down < 17:
      for num in up_border_tile2:
        tileID = (animation_row_to_down * 6) + num
        toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
        print("tileid: " +toAppend)
        color_array[tileID - 1] = toAppend
        print(color_array)
    if animation_row_to_up > 0:
      for num in up_border_tile2:
        tileID = ((animation_row_to_up + 1) * 6) + num
        toAppend = str(tileID) + " " + "1 " + MainColorRed + " " + MainColorGreen + " " + MainColorBlue + " 0 200"
        color_array[tileID - 1] = toAppend
        print(animation_row_to_up)
    if animation_row_to_up == 0:
      is_done += 1 
    if animation_row_to_down > 17:
      is_done += 1
    if is_done == 2:
      animation_is_done = True
    animation_row_to_up -= 1
    animation_row_to_down += 1
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
  radial_Wave_Animation(int(RightOneTouchedG[0]), "100", "150", "150", "1", "1", "1")
  background3("100", "150", "150")

main()








