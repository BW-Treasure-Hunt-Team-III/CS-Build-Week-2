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
        self.player_cooldown = 1,
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

        print(data)
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
            

            if self.map.checkIfRoomMapped(currentRoom['room_id']) is not True:
                print('has not been mapped')
                #because current room is not mapped, add  to map:
                self.map.addToMap(currentRoom)
                #check if we came from a previous direction

            if previousRoom:
                #update ids if we came from a previous room. 
                self.map.updateRoomExits(previousRoom['room_id'], currentRoom['room_id'], direction)

            #if all exits have been explored
            while self.map.unexploredExits(currentRoom['room_id']):
                with open("reverse.txt", "r+") as f:
                    data = f.read()
                    print("we will now move in reverse")
                    reverse_direction = data[-1]

                time.sleep(self.player_cooldown) #this waits the cooldown timer amount
                currentRoom = self.travel(str(reverse_direction))

                print(currentRoom)
                with open('reverse.txt', "w") as f:
                    f.write(data[:-1])
                    f.close()
                self.player_location = currentRoom['room_id']
                self.player_cooldown = currentRoom['cooldown']

            #go to first available exit in this current room. 
            direction = self.map.getOneExit(currentRoom['room_id'])

            #write our direction to this file so that we can have a reverse path
            with open("reverse.txt", "a") as f:
                f.write(f'{directions[direction]}')
            previousRoom = currentRoom
            time.sleep(self.player_cooldown) #this waits the cooldown timer amount
            currentRoom = self.travel(direction)
            self.player_cooldown = currentRoom['cooldown']
            self.player_location = currentRoom['room_id']

    def travel(self, direction):
        if direction == 'n':
            json = {"direction":"n"}
            
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)

            print(json)
            response = requests.post(self.url + 'move', headers=self.headers, json=json)
            data = response.json() 
            return data

        if direction == 'e':
            json = {"direction":"e"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
            response = requests.post(self.url + 'move', headers=self.headers, json=json) 
            data = response.json() 
            return data
        if direction == 's':
            print(f'we are moving {direction}')
            json = {"direction":"s"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
            print(json)
            response = requests.post(self.url + 'move', headers=self.headers, json=json) 
            data = response.json() 
            return data
        if direction == 'w':
            json = {"direction":"w"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
                
            print(json)
            response = requests.post(self.url + 'move', headers=self.headers, json=json) 
            data = response.json() 
            return data

