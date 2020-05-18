import requests
import time
import random

t = .5
color_array = []
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

def begin_playline():
  return (37)

def end_playline():
  return (61)

def row_lines(begin_row, end_row, r, g, b):
  for column in range(6):
    begin_line = int(begin_row) + (1 * int(column))
    color_data1 = str(begin_line) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    end_line = int(end_row) + (1 * int(column))
    color_data2 = str(end_line) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[begin_line] = color_data1
    color_array[end_line] = color_data2
    print(color_array)
    Send_module(color_array)  

def random_column():
  return random.randint(1, 6)

def moving_column(column, r, g, b):
  for row in range(11):
    panel = int(column) + (6 * int(row))
    time.sleep(t)
    color_data = str(panel) + " " + "1 " + r + " " + g + " " + b + " 0 200"
    color_array[panel] = color_data
    print(color_array)
    Send_module(color_array)



background("100", "100", "200")
Send_module(color_array)
row_lines(begin_playline(), end_playline(), "156", "112", "7")
moving_column(random_column(), "255", "0", "0") 