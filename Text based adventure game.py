# dictionary

rooms = {'start': 
         {'name': 'the front porch',
          'north': 'lounge room', 
          'contents': [],
        'text': 'your standing at the front porch./ntheres a wooden door in frot of you.'},
    
         'lounge room': 
         {'name': 'the lounge room',
          'east': '1st pt of hallway', 'south': 'start', 
        'text': 'you are in the lounge/kichen. there a tv,/n dinning room table. and the couch', 
        'contents':  ['couch', 'tv', 'dinning room table', 'rug']},
         
    '1st pt of hallway':
         {'name': 'the hall way',
          'west': 'lounge room',
          'south': 'bedroom', 
          'east': '2nd pt of hallway',
          'contents': ['hall way rug', 'picher frames'],
      'text': 'a very very suspisous hall way.'},
    
         'bedroom':
         {'name': 'the bedroom',
          'north': '1st pt of hallway', 
          'contents': ['sheets', 'bed', 'lego', 'tv'],
        'text': 'This is a your bed room, its an avrege/nbedroom, no tolet in here.'},
        
        '2nd pt of hallway' :
         {'name': 'the 2nd pt of hallway', 
          'east': 'parents bedroom',
          'north': 'tolet', 
        'text': 'you are in the 2nd pt of hallway. ', 
        'contents': ['picher frame', 'rug',]},  
  
         'parents bedroom': 
         {'name' : 'the parents bed room', 
          'west' : '2nd pt of hallway', 
        'text': 'you are in the parents bed room. ', 
        'contents': ['king sized beed', 'tv',]},   
   
         'tolet': 
         {'name' : 'the holy grail its self(the tolet)',
          "south" : '2nd pt of hallway', 
        'text': 'the holy grail(tolet). ', 
        'contents': ['tolet', 'plunger',]}}    
           
directions = ['north', 'south', 'east', 'west']
current_room = rooms['start']
carrying = []
 

print("             TOLET TOM")

print("Youve gust got back from a long day at school,/nuve taking the bus home and arive at the front door.")
print("you havent gone to the tolet all day,/nyouve been avoding them at school becouse there are the most discusting palce youve every seen.Theres tolet paper on the wallls, pee stans on the celings, and skid marks on the doors. You refuse to go there .but that means evry day after school its a rush to the tolet.")
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
  
    # the player movement(north,west,east,south)
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # not very cool movement
            print("You can't go that way.")
   
    # to Quit the game
    elif command.lower() in ('q', 'quit'):
        break

#INVENTORY SYSTEM

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
t = int(10)
  
# the  coundown
countdown(int(t))

    
 #NOTES!
    # get timer to say to the code to stop game
    # when th tolet is reached the gamenees to stop
   # add more room

   
