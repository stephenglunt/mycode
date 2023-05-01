#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      fight [npc]
      flirt [npc]
      give [item] to [npc]
      use [item]
      talk [npc]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print movement options
    print(f"You can go {', '.join(list(rooms[currentRoom]['direction'].keys()))}")
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    elif 'npc' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['npc'])
    else:
        print(f"The {currentRoom} is empty.")
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                'direction' : {
                    'south' : 'Kitchen',
                    'east'  : 'Dining Room'
                    },
                  'item'  : 'key'
                },

            'Kitchen' : {
                'direction' : {
                    'north' : 'Hall'
                    },
                'npc'  : 'monster',
                },
            'Dining Room' : {
                'direction' : {
                  'west' : 'Hall',
                  'south': 'Garden'
                  },
                  'item' : 'potion'
               },
            'Garden' : {
                'direction' : {
                  'north' : 'Dining Room'
                  }
            }
         }


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]['direction']:
            #set the current room to the new room
            currentRoom = rooms[currentRoom]["direction"][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'fight' :
        # make two checks:
        # 1. if the current room contains an npc
        # 2. if the npc matches the npc that the player wishes to fight
        if "npc" in rooms[currentRoom] and move[1] in rooms[currentRoom]['npc']:
            print('You are unarmed. How will you attack?\n(P)unch\n(K)ick\n')
            fightOption = input('>')


