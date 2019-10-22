import json

class Map:

    def __init__(self):
        self.data = {}
        self.loadMapFile()

    def loadMapFile(self):
        with open('map.txt') as json_file:
            self.data = json.load(json_file)
            # for location in data['locations']:
            #     print('Title: ' + location['title'])
            #     print('Description: ' + location['description'])
            #     print('Id: ' + location['id'])
            #     print('')

    def addToMap(self, newLocation):

        print('newLocation', newLocation)

        #with this function we can add a new object to our Room file, 
        # #it will take the file and overwrite it with the new self.data
        roomID = newLocation["room_id"]

        #check if room is already in self.data
        if str(roomID) in self.data:
            print("Room already exists")
        else:
            newLocation = {
                "title": newLocation['title'],
                "room_id": newLocation['room_id'],
                "elevation": newLocation['elevation'],
                "coordinates": newLocation['coordinates'],
                "terrain": newLocation['terrain'],
                "exits": newLocation['exits'],
                "messages": newLocation['messages']
            }

            self.data[roomID] = newLocation

            #write our self.data to the file. 
            with open('map.txt', 'w') as outfile:
                json.dump(self.data, outfile)

            #needs to be done so that we have our object properties have updated map
            self.loadMapFile()

    def findPath(self, startID, endID):
        #this function will find a path from start to finish, with id's and directions delivered for use by the scripter
        pass