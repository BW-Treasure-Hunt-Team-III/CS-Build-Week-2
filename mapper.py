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
        roomID = newLocation["room_id"]
        if str(roomID) in self.data:
            print("room already exists")
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

            with open('map.txt', 'w') as outfile:
                json.dump(self.data, outfile)
    