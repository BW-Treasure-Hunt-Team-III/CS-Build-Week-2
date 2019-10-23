import json

class Map:

    #this initiation function has an empty data file. but by running self.loadMapFile(), we fill it with our JSON object of locations which is basically a dictionary/graph
    def __init__(self):
        self.data = {}
        self.loadMapFile()
        self.length = len(self.data)

    def loadMapFile(self):
        with open('map.txt') as json_file:
            self.data = json.load(json_file)
            # for location in data['locations']:
            #     print('Title: ' + location['title'])
            #     print('Description: ' + location['description'])
            #     print('Id: ' + location['id'])
            #     print('')

    def checkIfRoomMapped(self, roomId):
        #this function lets you know if the room you are in has already been mapped. 
        if str(roomId) in self.data:
            return True
        else: 
            return False

    def addToMap(self, newLocation):

        #with this function we can add a new object to our Room file, 
        # #it will take the file and overwrite it with the new self.data
        roomId = newLocation["room_id"]

        #check if room is already in self.data
        # newLocation = {
        #     "room_id": newLocation['room_id'],
        #     "exits": {x:-1 for x in newLocation['exits']},
        # }

        self.data[roomId] = {x:-1 for x in newLocation['exits']}

        #write our self.data to the file. 
        with open('map.txt', 'w') as outfile:
            json.dump(self.data, outfile)

        #needs to be done so that we have our object properties have updated map
        self.loadMapFile()

    def findPath(self, startID, endID):
        #this function will find a path from start to finish, with id's and directions delivered for use by the scripter
        pass
    
                              #0     , #5,      n
    def updateRoomExits(self, oldRoom, newRoom, direction):

        directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

        self.data[oldRoom][direction] = newRoom
        self.data[newRoom][directions[direction]] = oldRoom

    def unexploredExits(self, roomId):
        for ea in self.data[roomId]:
            if ea == -1:
                return False
        return True

    def getOneExit(self, roomId):
        for key, value in self.data[roomId]:
            if value == -1:
                return key