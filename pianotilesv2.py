import requests
import time
import random

# t is de time voor sleep.
t = .2
color_array = []
touchable_tiles = [49, 50, 51, 52, 53, 54]
score = 0
link_colorstring = 'http://nanoleaf.nandhoman.nl:3000/ColorString'
nanoleafs = 102
nanostring = "102"

def background(r, g, b):
  for id in range(nanoleafs):
    toAppend = str((id + 1)) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array.append(toAppend)

def Send_module(color_array):
  colorstring = nanostring
  for id in color_array:
    colorstring += " " + id
  myobj = {"command": "display",
  "animType": "static",
  "animData": colorstring,
  "loop": False}
  requests.post(link_colorstring, data = myobj)

def begin_playline():
  return (43)

def end_playline():
  return (55)

def row_lines(begin_row, end_row, r, g, b):
  for column in range(6):
    begin_line = int(begin_row) + (1 * int(column))
    color_data1 = str(begin_line) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    end_line = int(end_row) + (1 * int(column))
    color_data2 = str(end_line) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[begin_line] = color_data1
    color_array[end_line] = color_data2

  Send_module(color_array)  

def random_column():
  return random.randint(37, 42)


def moving_column(tijd, column, turn, r, g, b , pr, pg, pb):
  for row in range(4):
    panel_pianotile = int(column) + (6 * int(row))

    # het functie sleept hier zodat de vallende tile niet te snel gaat.
    time.sleep(t)
    
    # Bovenste en onderste lijn opnieuw tekenen.
    row_lines(begin_playline(), end_playline(), "156", "112", "7")


    color_data_pianotile = str(panel_pianotile) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[panel_pianotile] = color_data_pianotile
    panel_bg = int(column) + (6 * (int(row)-1 ))
    color_data_bg = str(panel_bg) + " " + "1 " + pr + " " + pg + " " + pb + " 0 200"
    color_array[panel_bg] = color_data_bg

    if row == 2:
      row_lines(begin_playline(), end_playline(), "156", "112", "7")


    # Clickbaar maken.
    print("current color is")
    print(panel_pianotile)
    x = requests.get('http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles')
    clicked_tile = x.text
    print("clicked color is")
    print(clicked_tile[35:37])
    if clicked_tile[35:37] == str(panel_pianotile - 6):
      if (int(panel_pianotile - 6) in touchable_tiles):
       panel_pg = int(panel_pianotile)
       color_data_pg = str(panel_pg) + " " + "1 " + pr + " " + pg + " " + pb + " 0 200"
       color_array[panel_pg] = color_data_pg

       # score bijhouden.
       score =+ 1
       print("score is")
       print(score)

       # functie stoppen.
      break
    
    Send_module(color_array)
    
   
  
  time.sleep(t)
  row_lines(begin_playline(), end_playline(), "156", "112", "7")


background("100", "100", "200")
Send_module(color_array)
row_lines(begin_playline(), end_playline(), "156", "112", "7")
for x in range(60):
  moving_column(x, random_column(), 3, "255", "0", "0", "100", "100", "200")

