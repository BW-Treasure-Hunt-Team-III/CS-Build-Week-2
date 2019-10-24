def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        visited = []
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            shortest_path = stack.pop()
            vertex = shortest_path[-1]
            if vertex not in visited:
                if vertex is destination_vertex:
                    print("DFS")
                    return shortest_path
                visited.append(vertex)
                for neighbor in self.vertices[vertex]:
                    new_shortest_path = list(shortest_path)
                    new_shortest_path.append(neighbor)
                    stack.push(new_shortest_path)
        
        return None