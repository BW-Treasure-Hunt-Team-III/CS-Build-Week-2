#If player reached the dead end, keeps track of directions for traveling back. 
reverse_path = [] 


#go through the json file and fill out all the visited rooms 
visited = {0: {"n": -1, "s": -1, "e": -1, "w": -1}}
            10: {n: -1, s: 0, e: -1, w: -1}
            15: {s: 0}



while len(visited) < 499:
    what is self.player_cooldown? wait that amount. 
    
    if player.currentRoom.id not in visited:

        visited[player.currentRoom.id] = player.currentRoom.getExits() # 10: {n: -1, s: -1, e: -1, w: -1}

        #visited[player.currentRoom.id].remove(reverse_path[-1]) #makes sure that we dont hit the old direction we just came from 

    #Player reached the room with no exits
    while len(visited[player.currentRoom.id]) == 0: #has no exits == -1
        reverse_direction = reverse_path.pop()
        player should travel in reverse_direction #call the endpoint to move in this reverse direction

    #First available direction to exit the room
    direction = visited[player.currentRoom.id] #pull out an exit with a value of -1 (pull out the key) 
    reverse_path.append(directions[direction]) [s]
    player should travel in direction #call the endpoint to move in this direction