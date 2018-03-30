###########################################################################################
# Name: Christopher Rice - Room Adventure
# Date: 3/27/18
# Description: An adventure game! You start in a house and try and escape.
###########################################################################################
from Tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
        # the constructor
        def __init__(self, name, image):
                # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
                # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
                # and grabbables (things that can be taken into inventory)
                self.name = name
                self.image = image
                self.exits ={}
                self.items = {}
                self.grabbables = []

        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value

        @property
        def image(self):
                return self._image

        @image.setter
        def image(self, value):
                self._image = value

        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value

        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value

        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate dictionary
                self._exits[exit] = room

        def delExit(self, exit):
                del self._exits[exit]

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate dictionary
                self._items[item] = desc

        def delItem(self, item):
                del self._items[item]

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items.keys():
                        s += item + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits.keys():
                        s += exit + " "

                return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        # the constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the rooms
        def createRooms(self):
                # yeah, I hate all the globals as well, but there's not much I can do
                # as to avoid it. I have to be able to call them outside of the class.
                # there's no way the user can mess with them, so it should be okay.
                global r1
                global r2
                global r3
                global r4
                global r5
                global r6
                global r7
                global r8
                global r9
                global r10
                global r0

                r1 = Room("Room 1", "room1.gif")
                r2 = Room("Room 2", "room2.gif")
                r3 = Room("Room 3", "room3.gif")
                r4 = Room("Room 4", "room4.gif")
                r5 = Room("Upstairs: Room 5", "room5.gif")
                r6 = Room("Upstairs: Room 6", "room6.gif")
                r7 = Room("Upstairs: Room 7", "room7.gif")
                r8 = Room("Roof", "room8.gif")
                r9 = Room("Top of the Roof", "room9.gif")
                r10 = Room("Attic", "room10.gif")
                r0 = Room("the road. You escaped!", "room0.gif")

                
                # Room Diagrams:
                '''
                0
                |
                locked
                |
                1  2
                3  4
                |  |
                |   -> death
                |
                5  6
                   7
                   |
                   |
                   8 --> 9 -> 10
                   |
                   death
                '''
                
                # add exits to room 1
                r1.addExit("east", r2) # to the east of room 1 is room 2
                r1.addExit("south", r3)
                # add grabbables to room 1
                r1.addGrabbable("key")
                # add items to room 1
                r1.addItem("chair", "It's a chair, and you could sit on it, I guess.")
                r1.addItem("table", "It's a table. I don't know what you expected.")
                r1.addItem("cat", "For some reason, in this empty house, there's a \ncat that's decided to make itself visible \nand friendly. Nice.")
                r1.addItem("door", "Maybe I came in this door...maybe I can get back out.")
                
                # add exits to room 2
                r2.addExit("west", r1)
                r2.addExit("south", r4)
                # add items to room 2
                r2.addItem("rug", "It is nice and Indian. Looks like Aladdin's \ncarpet, past all the dust.")
                r2.addItem("fireplace", "It is full of ashes...smells kinda like monkey. \nOuch.")
                r2.addItem("switch", "Not sure what it does. It's currently off...you \ncould turn it on if you wanted. \nTry saying 'flipon switch'.")
                r2.addItem("shirt", "There's a random shirt lying on the ground. Says something unreadable on the front of it.")
                
                # add exits to room 3
                r3.addExit("north", r1)
                r3.addExit("east", r4)
                # add grabbables to room 3
                r3.addGrabbable("book")
                # add items to room 3
                r3.addItem("bookshelves", "A bookshelf with a singular book. You could pick it up and read it by saying 'read book'.")
                r3.addItem("statue", "The eyes of the statue seem to follow you around the room...")
                r3.addItem("desk", "The statue is resting on it. Otherwise, \nnothing to see.")
                r3.addItem("stairs", "There's a staircase here...you can't go up \nbecause the door at the top is locked. \nMaybe there's a key?")
                
                # add exits to room 4
                r4.addExit("north", r2)
                r4.addExit("west", r3)
                r4.addExit("south", None) # Death to the poor soul who doesn't heed the warning
                # add grabbables to room 4
                r4.addGrabbable("key")
                # add items to room 4
                r4.addItem("paper", "There's a paper lying on the floor. \nIt's been crumpled up. \nIt says something about a pitfall and \nsome staircase.")
                r4.addItem("sign", "A sign is hanging on the wall next to the \nsouthern exit door. \nIt says in red: 'DO NOT ENTER.' \nSuspicious.")
                r4.addItem("drum", "There's a drum sitting on its side in the room. \nThere's a key at the bottom...\nmaybe we could use that.")

                # room 5
                r5.addExit('downstairs', r3)
                r5.addExit('east', r6)
                r5.addExit('hallway', r7)
                r5.addItem("piano", "It looks like it hasn't been played in years. \nYou hit a key and all you hear is a clunk.")
                r5.addItem("computer", "You try and turn it on, and to your surprise \nit boots up! \nOf course, it's locked. The username is 'Pardunk' \nbut you don't know the password...")
                r5.addItem("desk", "The computer is sitting on this desk, along with a keyboard and mouse. \nThey look perfectly fine other than the layer of dust covering them.")
                r5.addItem("chair", "It's a wooden chair. \nLooks like it could still hold someone.")
                r5.addItem("stairs", "The staircase you came up to get here is...\nwell...still there. \nSurprising eh? You could always head back down \nif you'd like.")

                # room 6
                r6.addExit("west", r5)
                r6.addExit("south", r7)
                r6.addItem("bed", "This looks like it was rushed out of one morning and never touched since.")
                r6.addItem("chest-of-drawers", "It's full of clothes. In the bottom drawer, \nthere is a single document. \nYou could pick it up and read it with \n'document read'.")
                r6.addItem("desk", "Someone used to do lots of paperwork here. \nDoesn't look like anyone's been here for a while,\nas the papers are covered in dust.")
                r6.addGrabbable("document")

                # room 7 / hallway
                r7.addExit('north', r6)
                r7.addExit('hallway', r5)
                r7.addExit('window', r8)
                r7.addItem("picture", "It looks like a photo of someone used to be \nin here, but all that's left is some dust \nin a frame.")
                r7.addItem("lamp", "There's no bulb inside, so it doesn't look like \nit's worth anything.")
                r7.addItem("safe", "It's a safe that's been broken open and emptied. Nothing is within.")

                # room 8 / roof
                r8.addExit('window', r7)
                r8.addExit('jump', None)
                r8.addExit('up', r9)
                r8.addItem('around', "There isn't much to see. \nThere is some trees, a house in the distance... \nThe house you're in seems really out of place.")
                r8.addItem('up', "The sky is cloudy and gray. You're near the edge of the roof... \nyou could go further up the roof if you wanted.")
                r8.addItem('down', "Even though you're on the second floor, it seems way too high to hop down. \nThis is one weird building.")

                # room 9 / rooftop
                r9.addExit('down', r8)
                r9.addItem('out', "You see the rest of the roof... other buildings similar to this one \nbut much nicer and cleaner. This one stands out.")
                r9.addItem('fan', "If you could get the fan to stop spinning, it \nlooks like it's big enough for you to climb down \ninto the attic.")
                
                # room 10 / attic
                r10.addExit('fan', r9)
                r10.addItem('fan', "It's the fan you came through. It's not spinning. \nAll you can see through the hole are \nthe looming clouds.")
                r10.addItem('tv', "It's a television that hasn't been turned \non in ages. \nYou try to push a button on it \nbut nothing happens.")
                r10.addItem('boxes', "The attic is filled with old antiques...\nnone seem of any importance.")
                r10.addItem("crowbar", "There's a crowbar on the ground. \nMaybe I could pry a door open with this?")
                r10.addGrabbable("crowbar")

                # room 0 / win
                r0.addItem("You escaped!", "Congrats!")
                r0.addExit("Congrats!", r10)
                
                # set room 1 as the current room at the beginning of the
                # game
                Game.currentRoom = r1
                # initialize the player's inventory
                Game.inventory = []

        # sets up the GUI
        def setupGUI(self):
                # organize the GUI
                self.pack(fill=BOTH, expand=1)
                # setup the player input at the bottom of the GUI
                # the widget is a Tkinter Entry
                # set its background to white and bind the return key to the
                # function process in the class
                # push it to the bottom of the GUI and let it fill
                # horizontally
                # give it focus so the player doesn't have to click on it
                Game.player_input = Entry(self, bg="white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()
                # setup the image to the left of the GUI
                # the widget is a Tkinter Label
                # don't let the image control the widget's size
                img = None
                Game.image = Label(self, width=WIDTH / 2, image=img)
                Game.image.image = img
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)
                # setup the text to the right of the GUI
                # first, the frame in which the text will be placed
                text_frame = Frame(self, width=WIDTH / 2)
                # the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the frame's size
                Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                Game.text.pack(fill=Y, expand=1)
                text_frame.pack(side=RIGHT, fill=Y)
                text_frame.pack_propagate(False)

        # set the current room image
        def setRoomImage(self):
                if (Game.currentRoom == None):
                        # if dead, set the skull image
                        Game.img = PhotoImage(file="skull.gif")
                else:
                        # otherwise grab the image for the current room
                        Game.img = PhotoImage(file=Game.currentRoom.image)
                        # display the image on the left of the GUI
                Game.image.config(image=Game.img)
                Game.image.image = Game.img

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                # enable the text widget, clear it, set it, and disabled it
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                if (Game.currentRoom == None):
                        # if dead, let the player know
                        Game.text.insert(END, "You are dead. \nThe only thing you can do now is quit.\nTry again?")
                else:
                        # otherwise, display the appropriate status
                        Game.text.insert(END, str(Game.currentRoom) +\
                        "\nYou are carrying: " + str(Game.inventory) +\
                        "\n\n" + status)
                Game.text.config(state=DISABLED)

        # plays the game
        def play(self):
                # add the rooms to the game
                self.createRooms()
                # configure the GUI
                self.setupGUI()
                # set the current room
                self.setRoomImage()
                # set the current status
                self.setStatus("")

        # processes the player's input
        def process(self, event):
                # grab the player's input from the input at the bottom of
                # the GUI
                action = Game.player_input.get()
                # set the user's input to lowercase to make it easier to
                # compare the verb and noun to known values
                action = action.lower()
                # set a default response
                response = "I don't understand. Make sure you've spelled it \nright and are using the verb noun format. \nOtherwise, see help by typing 'help'."
                # exit the game if the player wants to leave (supports quit,
                # exit, and bye)
                if (action == "quit" or action == "exit"):
                        exit(0)
                if (action == "help"):
                        response = "The available commands are:\
                        \ngo, 'go south' \nlook, 'look table' \ntake, 'take key' \nhelp, shows this! \nchangelog, shows update log \nread, 'read book' \n \nUse these in a verb noun format.\
                        \nIf you see an item that you could pick up, \nlike a book or etc, \ntry picking it up by saying 'take name', \n'name' being the item."
                if (action == "changelog"):
                        response = "Welcome to House Adventure (v1.04), a simple \nPython 2.7.14 game written by Rwarcards762. \nRelease / Update Notes:\
                        \nPre-GUI Patch Notes:\
                        \n-Hallway renamed, crowbar and fan errors fixed, \nremoved and added some easter eggs.\
                        \nGUI-Era Patch Notes:\
                        \n= v 1.04 =\
                        \n-Converted old code to the new Room Adventure!\
                        \n= v 1.05 =\
                        \n-Fan description now accurate to state \n-Text bugs squashed\
                        \n-help is now more helpful\
                        \n-Win screen disables entry bar \n-intro message now features 'read' \n-read fucntion improved significantly\
                        \n= v 1.06 release =\
                        \n-desk added \n-room image placeholders removed \n-final text edits \n-GitHub repo added!"
                if (Game.currentRoom == None): # player goes to a death room
                        # clear the player's input
                        Game.player_input.delete(0, END)
                        return

                # split the user input into words (words are separated by
                # spaces) and store the words in a list
                words = action.split()
                # the game only understands two word inputs
                if (len(words) == 2):
                        # isolate the verb and noun
                        verb = words[0]
                        noun = words[1]
                        # the verb is: go
                        if (verb == "go"):
                                # set a default response
                                response = "Invalid exit."
                                # check for valid exits in the current room
                                if (noun in Game.currentRoom.exits):
                                        # if one is found, change the current room to
                                        # the one that is associated with the
                                        # specified exit
                                        Game.currentRoom =\
                                                Game.currentRoom.exits[noun]
                                        # set the response (success)
                                        response = "Room changed."
                        # the verb is: look
                        elif (verb == "look"):
                                # set a default response
                                response = "I don't see that item."
                                # check for valid items in the current room
                                if (noun in Game.currentRoom.items):
                                        # if one is found, set the response to the
                                        # item's description
                                        response = Game.currentRoom.items[noun]
                        # the verb is: take
                        elif (verb == "take"):
                                # set a default response
                                response = "I don't see that item."
                                # check for valid grabbable items in the current riin
                                for grabbable in Game.currentRoom.grabbables:
                                        # a valid grabbable item is found
                                        if (noun == grabbable):
                                                # add the grabbable item to the player's inv
                                                Game.inventory.append(grabbable)
                                                # remove the grabbable item from the room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                # set the response (success)
                                                response = "Item grabbed."
                                                # now check for fancy changes
                                                # allows for items in the room to change based
                                                # on items that have been removed from the room
                                                if (noun == 'book'):
                                                        if ('book' in Game.inventory):
                                                                r3.delItem("bookshelves")
                                                                r3.addItem("bookshelves", "Empty bookshelves covered in dust.\
                                                                        \nYou've already taken the book from the shelves.")
                                                elif (noun == 'key'):
                                                        if ('key' in Game.inventory):
                                                                r3.addExit('upstairs', r5)
                                                                r3.delItem('stairs')
                                                                r4.delItem('drum')
                                                                r3.addItem('stairs', "There's an old staircase. You've gotten the key, \nso now you can go upstairs as you please.")
                                                                r4.addItem('drum', "It's an empty container.")
                                                elif (noun == 'document'):
                                                        if ('document' in Game.inventory):
                                                                r6.delItem("chest-of-drawers")
                                                                r6.addItem("chest-of-drawers", "It's full of clothes.\
                                                                                \nYou've taken the document out already.")
                                                elif (noun == "crowbar"):
                                                        if ('crowbar' in Game.inventory):
                                                                r10.delItem('crowbar')
                                                                r1.addExit('break-door', r0)
                                                                r1.delItem('door')
                                                                r1.addItem('door', "The crowbar I picked up should be able \nto break this door open. \nLet's find out...")
                                                break
                        elif (verb == "read"): # checks if you have the book, then lets you read
                                if ((noun == "book") and ('book' in Game.inventory)):
                                        response = "You attempt to read the book...\
                                        \nIt says something about a pitfall...\
                                        \nA locked door, a staircase...some fan...\
                                        \nMost of the book has been torn out."
                                elif ((noun == "document") and ("document" in Game.inventory)):
                                        response = "You read the document you found.\
                                                \n...it talks about some plan to run off...\
                                                \nSome roof, some pitfall, some trap,\
                                                \nand is signed in some scrawl that is\
                                                \nimpossible to make out."
                                else:
                                        response = "You don't have that item in your inventory, \nor that item is unreadable. \nOr maybe you spelled something wrong?"
                        elif (verb == 'flipon' and noun == 'switch'):
                                if (Game.currentRoom == r2):
                                        r2.delItem('switch')
                                        r9.addExit('fan', r10)
                                        r2.addItem('switch', "Not sure what it does, but it's now on.\
                                                \nYou could turn it off with 'flipoff switch'.")
                                        r9.delItem('fan')
                                        r9.addItem('fan', "It's some attic fan. Looks like you \ncan climb through, as it's not spinning.")
                                        response = "You flipped the switch. You heard a thunk...\
                                                \n...something came to a stop. Somewhere."
                        elif (verb == 'flipoff' and noun == 'switch'):
                                if (Game.currentRoom == r2):
                                        r2.delItem('switch')
                                        r9.delExit('fan')
                                        r9.delItem('fan')
                                        r9.addItem('fan', "If you could get the fan to stop spinning, it \nlooks like it's big enough for you to climb down \ninto the attic.")
                                        r2.addItem('switch', "Not sure what it does, but\
                                                \nit's currently off. You could turn it\
                                                \nback on with 'flipon switch.'")
                                        response = "You flipped off the switch.\
                                                \nYou heard something whir back to life..."
                # display the response on the right of the GUI
                # display the room's image on the left of the GUI
                # clear the player's input
                
                if (Game.currentRoom != r0):
                        self.setStatus(response)
                        self.setRoomImage()
                        Game.player_input.delete(0, END)

                if (Game.currentRoom == r0):
                        response = "Congrats! You escaped the house... \nlet's not go back in."
                        self.setStatus(response)
                        self.setRoomImage()
                        Game.player_input.delete(0, END)
                        Game.player_input.config(state=DISABLED)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
g.setStatus("Welcome to a house that seemingly makes no sense.\
        \nYou've stumbled into this house from-- \nwell, somewhere. \nYou can't quite remember why you came here, \nbut you know you were supposed to.\
        \nThere are things all about the house that you can interact with.\
        \nYour goal? Get out of the house. \nYou know you came for a reason, \nbut you can't remember and you'd \nrather not be here.\n\
        \nIt seems as if this house was abandoned years and years ago, although the electricity is still on \nso you can somewhat see.\
        \nInteract with the world and make it out--somehow.\
        \nGood luck.\
        \nHow to play: respond using the format verb noun. \nAvailable verbs are go, look, take, and read. \n(example: go south)\
        \nTo view the help, just type help. \nTo exit, type exit or quit.\
        \nTo view the changelog, say changelog.")

# wait for the window to close
window.mainloop()
