import json
from stack import Stack


class Map:

    #this initiation function has an empty data file. but by running self.loadMapFile(), we fill it with our JSON object of locations which is basically a dictionary/graph
    def __init__(self):
        self.data = {}
        self.important = {}
        self.loadMapFile()
        self.length = len(self.data)

    def loadMapFile(self):
        with open('map.txt') as json_file:
            self.data = json.load(json_file)
        with open('map2.txt') as json_file:
            self.important = json.load(json_file)
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

        if newLocation['title'] != "A misty room":
            self.important[roomId] = newLocation['title']

        self.data[roomId] = {x:-1 for x in newLocation['exits']}

        #write our self.data to the file. 
        with open('map.txt', 'w') as outfile:
            json.dump(self.data, outfile)
        
        with open('map2.txt', 'w') as outfile:
            json.dump(self.important, outfile)

        #needs to be done so that we have our object properties have updated map
        self.loadMapFile()

    def knowId(self, roomId, direction):
        if self.data[str(roomId)][direction] != -1:
            return str(self.data[str(roomId)][direction])
        return False

    def findPath(self, startID, endID):
        #this function will find a path from start to finish, with id's and directions delivered for use by the scripter
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = []
        stack = Stack()
        stack.push([startID])

        while stack.size() > 0:
            shortest_path = stack.pop()
            vertex = shortest_path[-1]
            if vertex not in visited:
                print(f'{vertex} and {endID}')
                if vertex is endID:
                    return shortest_path
                visited.append(vertex)
                for key, value in self.data[str(vertex)].items():
                    new_shortest_path = list(shortest_path)
                    new_shortest_path.append(value)
                    stack.push(new_shortest_path)
        
        return None
    
                              #0     , #5,      n
    def updateRoomExits(self, oldRoom, newRoom, direction):

        print(f'updating exits for room {oldRoom} and {newRoom} after travelling {direction}')
        directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

        self.data[str(oldRoom)][direction] = newRoom
        self.data[str(newRoom)][directions[direction]] = oldRoom

    def unexploredExits(self, roomId):
        for key, value in self.data[str(roomId)].items():

            if value == -1:
                return False
        return True

    def getOneExit(self, roomId):
        for key, value in self.data[str(roomId)].items():
            if value == -1:
                return key