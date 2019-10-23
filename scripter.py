import sys
import requests
import time
from mapper import Map

class Scripter:
    #Main Script Class

    def __init__(self, key, command='go to the nearest shrine'):
        #this will insert the api key into requests
        self.apiKey = key

        self.url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/" #add additional url information at the end. 
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Token ' + self.apiKey} 

        #map json will be used to pass map graph to other users. 
        self.map = Map()

        #whch command/script is currently running
        self.command = command

        #status of player: 
        self.player_name = "",
        self.player_cooldown = 0,
        self.player_encumbrance = 0,  # How much are you carrying?
        self.player_strength = 0,  # How much can you carry?
        self.player_speed = 0,  # How fast do you travel?
        self.player_gold = 0,
        self.player_inventory = [],
        self.player_status = [],
        self.player_errors = [],
        self.player_messages = []
        self.player_location = ''

    def getStatus(self):
        response = requests.get(self.url + 'init', headers=self.headers) 
        # extracting data in json format 
        data = response.json() 

        #set the player location & cooldown
        self.player_location = data['room_id']
        self.player_cooldown = data['cooldown']

        #this add to map function sends our current information to our Map Class and makes sure that it is mappd. 
        return data


    def mapper(self):
        #travel backwards to new exits
        reverse_path = [] 
        directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

        currentRoom = self.getStatus()

        previousRoom = ''
        direction = ''

        while self.map.length < 499: #make sure we dont have all 500 rooms mapped already
            time.sleep(self.player_cooldown) #this waits the cooldown timer amount

            if self.map.checkIfRoomMapped(currentRoom['room_id']):
                #because current room is not mapped, add  to map:
                self.map.addToMap(currentRoom)
                #check if we came from a previous direction
                if previousRoom:
                    #update ids if we came from a previous room. 
                    self.map.updateRoomExits(previousRoom['room_id'], currentRoom['room_id'], direction)

            #if all exits have been explored
            while self.map.unexploredExits(currentRoom['room_id']):
                reverse_direction = reverse_path.pop()
                self.travel(reverse_direction)

            #go to first available exit in this current room. 
            direction = self.map.getOneExit()
            reverse_path.append(directions[direction])
            self.travel(direction)
            


    def travel(self, direction):
        if direction == 'n':
            response = requests.get(self.url + 'init', headers=self.headers) 

