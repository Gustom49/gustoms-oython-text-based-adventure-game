from time import sleep
from threading import *

from re import T
 #dictionary

rooms = {'start': 
         {'name': 'the front porch',
          'north': 'lounge room', 
          'contents': [],
        'text': 'your standing at the front porch.theres a wooden door in frot of you.\n derections were you can go: north:'},
    
         'lounge room': 
         {'name': 'the lounge room',
          'east': '1st pt of hallway', 
          'south': 'start', 
          'north': 'kichen',
        'text': 'you are in the lounge. there a tv,\n dinning room table. and the couch\n derections were you can go: east, south, north:', 
        'contents':  ['couch', 'tv', 'dinning room table', 'rug']},

        'kichen': 
         {'name': 'the kichen',
          'north': 'cuboard',
           'south': 'lounge', 
        'text': 'you are in the kichen. there be food, a\n derections were you can go: north, south:', 
        'contents':  ['frig', 'oven', 'dishwasher', 'ketal', 'sink']},
         
         'cuboard': 
         {'name': 'the cuboard',
           'east': 'vegimit shapes',
           'south': 'kichen', 
        'text': 'you are in the cubord. there be food, a\n derections were you can go: east, south:', 
        'contents':  ['smith chips', 'pasta', 'dog food', 'biskit', 'tolet paper']},
         
         'vegimit shapes': 
         {'name': 'vegimit shapes',
           'west': 'cuboard', 
        'text': 'oven baked, not fried \n derections were you can go: west', 
        'contents':  ['flavour you can see',  'tasmanis shape' , 'australia shape']},
    
    '1st pt of hallway':
         {'name': 'the hall way',
          'west': 'lounge room',
          'south': 'bedroom', 
          'east': '2nd pt of hallway',
          'contents': ['hall way rug', 'picher frames'],
      'text': 'a very very suspisous hall way.\n derections were you can go: west,south,east:'},
    
         'bedroom':
         {'name': 'the bedroom',
          'north': '1st pt of hallway', 
          'contents': ['sheets', 'bed', 'lego', 'tv'],
        'text': 'This is a your bed room, its an avrege\nbedroom, no tolet in here.\n derections were you can go: north:'},
        
        '2nd pt of hallway' :
         {'name': 'the 2nd pt of hallway', 
          'east': 'parents bedroom',
          'north': 'tolet', 
        'text': 'you are in the 2nd pt of hallway. \n derections were you can go: north,east',
        'contents': ['picher frame', 'rug',]},  
  
         'parents bedroom' :
         {'name' : 'the parents bed room', 
          'west' : '2nd pt of hallway', 
        'text': 'you are in the parents bed room. \nderections were you can go: west', 
        'contents': ['king sized beed', 'tv',]},   
   
         'tolet': 
         {'name' : 'the holy grail its self(the tolet)',
          "south" : '2nd pt of hallway', 
        'text': 'the holy grail(tolet).   \n derections were you can go: nowere else \n Please press enter to end game', 
        'contents': ['tolet', 'plunger',]}}    
           
directions = ['north', 'south', 'east', 'west']
current_room = rooms['start']
carrying = []
 

print("             TOLET TOM")

print("Youve gust got back from a long day at school,\nuve taking the bus home and arive at the front door.")
print("you havent gone to the tolet all day,\nyouve been avoding them at school becouse there are the most discusting palce youve every seen.\nTheres tolet paper on the wallls, pee stans on the celings, and skid marks on the doors.\n You refuse to go there .but that means evry day after school its a rush to the tolet.")
print("Your objective: Get to the TOLET in time TOM")

while True:
    # this displays current location
    print()
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    # this displays objects
    if current_room['contents']:
        print('In the room are: {}'.format(', '.join(current_room['contents'])))
    # gets input
    command = input('\nWhat do you do?(north,west,east,south): ').strip()
    # the player movement(north,west,east
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # not very cool movement
            print("You can't go that way.")
    # to Quit the game
    elif command.lower() in ('q', 'quit'):
        break
    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying.append(item)
        else:
            print("I don't see that here.")
    # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in carrying:
            current_room['contents'].append(item)
            carrying.remove(item)
        else:
            print("You aren't carrying that.")
    # icky comands
    else:
        print("I don't understand that command.")

   

# this is the timer tom

import time
  

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('times up, sorry bud, you didnt make it in time')
  
  
# the time in seconds(2mins)
t = int(120)
  
# the  coundown
countdown(int(t))

    
 #NOTES!
    # get timer to say to the code to stop game
    # when th tolet is reached the gamenees to stop
   # add more room