graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}

def DLS(start,goal,path,level,maxD):
    print("\nWe're on level",level)
    print("Goal node testing for",start)
    path.append(start)
    if start==goal:
        print("Goal node test successful!\n")
        return path
    print("Goal node testing failed")
    if level==maxD:
        return False
    print("\nExpanding node-->",start)
    for child in graph[start]:
        result = DLS(child,goal,path,level+1,maxD)
        if result:
            return result
        else:
            path.pop()
    return False

start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS('A',goal,path,0,maxD)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")
            