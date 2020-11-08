#this program is currently not complete so if it's wrong/not executing properly or not giving desired output that's the reason

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
            