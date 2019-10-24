import sys
import requests
import time
from mapper import Map
import random

from cpu import *

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

        #CPU translator
        self.cpu = CPU()

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

    def getInit(self):
        response = requests.get(self.url + 'init', headers=self.headers) 
        # extracting data in json format 
        data = response.json() 

        #set the player location & cooldown
        self.player_location = data['room_id']
        self.player_cooldown = data['cooldown']

        print(data)
        #this add to map function sends our current information to our Map Class and makes sure that it is mappd. 
        return data

    def getStatus(self):
        response = requests.post(self.url + 'status', headers=self.headers) 
        # extracting data in json format 
        data = response.json() 

        #set the player information
        self.player_name = data['name']
        self.player_encumbrance = data['encumbrance']
        self.player_strength = data['strength']
        self.player_gold = data['gold']
        self.player_inventory = data['inventory']
        self.player_status = data['status']
        self.player_errors = data['errors']
        self.player_messages = data['messages']

        print(data)
        #this add to map function sends our current information to our Map Class and makes sure that it is mappd. 
        return data

    def findPath(self, destination):
        path = self.map.findPath(self.player_location, destination)
        path.pop(0)
        print(path)
        for roomId in path:
            direction = self.map.findDirection(self.player_location, roomId)
            time.sleep(self.player_cooldown)
            currentRoom = self.travel(direction)
            self.player_cooldown = currentRoom['cooldown']
            self.player_location = currentRoom['room_id']

        print(f'room {destination} reached')

    def getCoin(self, amount)
        coinsMined = 0

        while coinsMined < amount:
            newLocation = self.wishingWell()
            self.findPath(newLocation)

    def getGold(self, amount):
        while self.player_gold < amount:
            if self.player_encumbrance < self.player_strength - 2:
                randomRoom = random.randint(2,499)
                #go to a random room path
                path = self.map.findPath(self.player_location, randomRoom)
                #check for an item. 
                path.pop(0)
                print(path)
                for roomId in path:
                    direction = self.map.findDirection(self.player_location, roomId)
                    time.sleep(self.player_cooldown)
                    currentRoom = self.travel(direction)
                    print(currentRoom)
                    self.player_cooldown = currentRoom['cooldown']
                    self.player_location = currentRoom['room_id']
                    for item in currentRoom['items']:
                        time.sleep(self.player_cooldown)
                        json = {"name":item}
                        response = requests.post(self.url + 'take', headers=self.headers, json=json)
                        data = response.json() 
                        self.player_cooldown = data['cooldown']
                    time.sleep(self.player_cooldown)
                    self.getStatus()
                    if self.player_encumbrance > self.player_strength - 2:
                        break
            else: 
                #go to shop
                path = self.map.findPath(self.player_location, 1)
                path.pop(0)
                print(path)
                for roomId in path:
                    direction = self.map.findDirection(self.player_location, roomId)
                    time.sleep(self.player_cooldown)
                    currentRoom = self.travel(direction)
                    self.player_cooldown = currentRoom['cooldown']
                    self.player_location = currentRoom['room_id']
                #sell all
                for item in self.player_inventory:
                    time.sleep(self.player_cooldown)
                    json = {"name":item}
                    response = requests.post(self.url + 'sell', headers=self.headers, json=json)
                    data = response.json() 
                    print(data)
                    self.player_cooldown = data['cooldown']

                    json["confirm"] = "yes"
                    time.sleep(self.player_cooldown)
                    response = requests.post(self.url + 'sell', headers=self.headers, json=json)
                    data = response.json() 
                    self.player_cooldown = data['cooldown']
                    time.sleep(self.player_cooldown)
                    self.getStatus()
                    print(self.player_gold)

    def wishingWell(self):
        path = self.map.findPath(self.player_location, 55)
        path.pop(0)
        print(path)
        for roomId in path:
            direction = self.map.findDirection(self.player_location, roomId)
            time.sleep(self.player_cooldown)
            currentRoom = self.travel(direction)
            self.player_cooldown = currentRoom['cooldown']
            self.player_location = currentRoom['room_id']
        json = {"name":"wishing well"}
        time.sleep(self.player_cooldown)
        response = requests.post(self.url + 'examine', headers=self.headers, json=json)
        data = response.json() 

        #write the wishing well message to wishingwell.txt
        with open('wishingwell.txt', 'w') as outfile:
             outfile.write(data['description'][39:])
             outfile.close()
        self.cpu.load('wishingwell.txt')
        

        self.player_cooldown = data['cooldown']
        time.sleep(self.player_cooldown)
        return ''.join(self.cpu.run()[23:])

    def changeName(self, newName):
        #467
        path = self.map.findPath(self.player_location, 467)
        #check for an item. 
        path.pop(0)
        print(path)
        for roomId in path:
            direction = self.map.findDirection(self.player_location, roomId)
            time.sleep(self.player_cooldown)
            currentRoom = self.travel(direction)
            self.player_cooldown = currentRoom['cooldown']
            self.player_location = currentRoom['room_id']
        json = {"name":newName}
        time.sleep(self.player_cooldown)
        response = requests.post(self.url + 'change_name', headers=self.headers, json=json)
        data = response.json() 
        print(data)
        self.player_cooldown = data['cooldown']
        time.sleep(self.player_cooldown)
        json["confirm"] = "aye"
        response = requests.post(self.url + 'change_name', headers=self.headers, json=json)
        data = response.json() 
        self.player_name = data['name']
        self.player_cooldown = data['cooldown']
        print('Your name has been changed')
        time.sleep(self.player_cooldown)
        self.getStatus()

    def mapper(self):
        #travel backwards to new exits
        reverse_path = [] 
        directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

        currentRoom = self.getInit()

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
        print(f'we are moving {direction}')

        if direction == 'n':
            json = {"direction":"n"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
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
            json = {"direction":"s"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
            response = requests.post(self.url + 'move', headers=self.headers, json=json) 
            data = response.json() 
            return data

        if direction == 'w':
            json = {"direction":"w"}
            if self.map.knowId(self.player_location, direction):
                json["next_room_id"] = self.map.knowId(self.player_location, direction)
            response = requests.post(self.url + 'move', headers=self.headers, json=json) 
            data = response.json() 
            return data

