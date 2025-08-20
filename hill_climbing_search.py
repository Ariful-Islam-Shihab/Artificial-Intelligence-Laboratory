maze=[
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,0,1,1],
    [0,1,0,0,0],
]

def hillClimbing(maze,start,end,maxIteraion):
    def heuristic(node):
        return abs(node[0]-end[0])+abs(node[1]-end[1])
    
    
    def getNeighbour(node):
        neigbours=[]
        moves=[(0,1),(1,0),(0,-1),(-1,0)]
        for move in moves:
            x=node[0]+move[0]
            y=node[1]+move[1]
            if valid((x,y)):
                neigbours.append((x,y))
        return neigbours
    
    
    
    def valid(node):
        if node[0]<0 or node[0]>=len(maze) or node[1]<0 or node[1]>=len(maze[0]) or maze[node[0]][node[1]]==1:
            return False
        return True
    path=[]
    result=0
    current=start
    for i in range(maxIteraion):
        if current==end:
            return path,True
        path.append(current)
        result+=1
        neighbours=getNeighbour(current)
        bstneighbour=min(neighbours,key=heuristic)
        
        if heuristic(bstneighbour)>heuristic(current):
            return path,False
        current=bstneighbour
    return path,False
    

start=(0,0)
end=(4,4)
maxIteration=100
path,result=hillClimbing(maze,start,end,maxIteration)
print(result)
print(path)