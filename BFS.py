def BFS(graph,start,dest) -> list(): #Input parameters for this method are 
                                     #1.Graph in which we're going to search for our destination(dest) node
                                     #2.start which is our start node and dest which is our destination node
    queue = list()
    visited = list()
    queue.append(start)
    visited.append(start)
    print('Visited',start)
    result = ["Not reachable",list()]
    while queue:
        node = queue.pop(0) 
        if node==dest:
            print('Destination node found',node)
            result[0] = 'Reachable'
            break
        print(node,'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
    result[1] = visited 
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}
result = BFS(graph, "A", "C")
print(result[0])
print("Path used to traverse :-" , result[1])        