import sys
import requests
import json
from mapper import Map

class Scripter:
    #Main Script Class

    def __init__(self, key, mapJson=[], command=''):
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

    def getStatus(self):
        response = requests.get(self.url + 'init', headers=self.headers) 
        # extracting data in json format 
        data = response.json() 
        #self.map.addToMap(data)


    def addToMap(self, room=None):
        #add room information to the map
        if self.command:
            url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
            r = requests.post(url, headers=self.headers, json = {"direction": self.command}) 
            new_room = r.json()
            print(new_room)
            self.map.addToMap(new_room)
        else:
            print("Not sure why its not working")

    # def run(self):

    #   wait command based on cooldown

    #     #move north //or fly

    #     #move east //or fly

    #     #move west //or fly

    #     #move south //or fly

    #     #take item

    #     #drop item

    #     #sell treasure

    #     #wear item

    #     #pray at shrine

    # def saveMapToJson(self):

    #     #create a json object and file and store map for future usage. 
