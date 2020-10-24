def DFS(graph,start,dest):
    stack = list()
    visited = list()
    stack.append(start)
    visited.append(start)
    print('Visited',start)
    result = ["Not reachable",list()]
    while stack:
        node = stack.pop() 
        if node==dest:
            print('Destination node found',node)
            result[0] = 'Reachable'
            break
        print(node,'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
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
result = DFS(graph, "A", "F")
print(result[0])
print("Path used to traverse :-" , result[1])        