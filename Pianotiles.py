import requests
import time

t = .5

#x = requests.get('http://nanoleaf.nandhoman.nl:3000/lastTouchedTiles')

#print(x.text)


url = 'http://nanoleaf.nandhoman.nl:3000/ColorString'

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 0 0 0 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 0 0 0 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 0 0 0 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 0 0 0 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 0 0 0 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 0 0 0 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 156 112 7 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 0 0 0 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 0 0 0 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 0 0 0 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 156 112 7 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)

myobj = {"command": "display",
  "animType": "static",
  "animData": "102 1 1 255 255 255 0 200 2 1 255 255 255 0 200 3 1 255 255 255 0 200 4 1 255 255 255 0 200 5 1 255 255 255 0 200 6 1 255 255 255 0 200 7 1 255 255 255 0 200 8 1 255 255 255 0 200 9 1 255 255 255 0 200 10 1 255 255 255 0 200 11 1 255 255 255 0 200 12 1 255 255 255 0 200 13 1 255 255 255 0 200 14 1 255 255 255 0 200 15 1 255 255 255 0 200 16 1 255 255 255 0 200 17 1 255 255 255 0 200 18 1 255 255 255 0 200 19 1 255 255 255 0 200 20 1 255 255 255 0 200 21 1 255 255 255 0 200 22 1 255 255 255 0 200 23 1 255 255 255 0 200 24 1 255 255 255 0 200 25 1 255 255 255 0 200 26 1 255 255 255 0 200 27 1 255 255 255 0 200 28 1 255 255 255 0 200 29 1 255 255 255 0 200 30 1 255 255 255 0 200 31 1 255 255 255 0 200 32 1 255 255 255 0 200 33 1 255 255 255 0 200 34 1 255 255 255 0 200 35 1 255 255 255 0 200 36 1 255 255 255 0 200 37 1 239 183 0 0 200 38 1 239 183 0 0 200 39 1 239 183 0 0 200 40 1 239 183 0 0 200 41 1 239 183 0 0 200 42 1 239 183 0 0 200 43 1 255 255 255 0 200 44 1 255 255 255 0 200 45 1 255 255 255 0 200 46 1 255 255 255 0 200 47 1 255 255 255 0 200 48 1 255 255 255 0 200 49 1 255 255 255 0 200 50 1 255 255 255 0 200 51 1 255 255 255 0 200 52 1 255 255 255 0 200 53 1 255 255 255 0 200 54 1 255 255 255 0 200 55 1 255 255 255 0 200 56 1 255 255 255 0 200 57 1 255 255 255 0 200 58 1 255 255 255 0 200 59 1 255 255 255 0 200 60 1 255 255 255 0 200 61 1 239 183 0 0 200 62 1 239 183 0 0 200 63 1 239 183 0 0 200 64 1 239 183 0 0 200 65 1 239 183 0 0 200 66 1 239 183 0 0 200 67 1 255 255 255 0 200 68 1 255 255 255 0 200 69 1 255 255 255 0 200 70 1 255 255 255 0 200 71 1 255 255 255 0 200 72 1 255 255 255 0 200 73 1 255 255 255 0 200 74 1 255 255 255 0 200 75 1 255 255 255 0 200 76 1 255 255 255 0 200 77 1 255 255 255 0 200 78 1 255 255 255 0 200 79 1 255 255 255 0 200 80 1 255 255 255 0 200 81 1 255 255 255 0 200 82 1 255 255 255 0 200 83 1 255 255 255 0 200 84 1 255 255 255 0 200 85 1 255 255 255 0 200 86 1 255 255 255 0 200 87 1 255 255 255 0 200 88 1 255 255 255 0 200 89 1 255 255 255 0 200 90 1 255 255 255 0 200 91 1 255 255 255 0 200 92 1 255 255 255 0 200 93 1 255 255 255 0 200 94 1 255 255 255 0 200 95 1 255 255 255 0 200 96 1 255 255 255 0 200 97 1 255 255 255 0 200 98 1 255 255 255 0 200 99 1 255 255 255 0 200 100 1 255 255 255 0 200 101 1 255 255 255 0 200 102 1 255 255 255 0 200 ",
  "loop": False}

game = requests.post(url, data = myobj)

time.sleep(t)
print(game.text)