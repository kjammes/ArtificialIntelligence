graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}

def DLS(start,end,graph,curDepth,dLimit):
    stack = [start]
    visited = [start]
    while stack:
        curNode = stack.pop()
        print("Testing for goal node at",curNode)
        if curNode==end:
            print("Goal test successful at node ",curNode)
            return visited
        else:
            print("Goal node testing failed.")
        if curDepth==dLimit:
            return []
        for child in graph[curNode]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
        curDepth += 1
        print("curDepth",curDepth)
    return []

path = DLS('A','E',graph,0,1)
if(path):
    print("{} is the path used to reach the destination".format(path))
else:
    print("No path available for the goal node in given depth limit")
            