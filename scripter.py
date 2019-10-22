import sys
import requests

class Scripter:
    #Main Script Class

    def __init__(self, key, mapJson=[], command=''):
        #this will insert the api key into requests
        self.apiKey = key

        self.url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/" #add additional url information at the end. 
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Token ' + apiKey} 

        #map json will be used to pass map graph to other users. 
        self.map = mapJson 

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
        response = requests.get(self.url + 'status', headers=headers) 
        # extracting data in json format 
        data = response.json() 
        print(data)


    # def addToMap(self, room):
    #     #add room information to the map

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
