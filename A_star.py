import heapq
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def heuristic(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)        
def graph():
    adjList=dict()
    a=int(input("Enter number of edges "))
    for i in range(a):
        u,v,w=input().split()
        w=int(w)
        if u not in adjList.keys():
            adjList[u]=[]
        adjList[u].append((v,w))
    return adjList

myList=graph()
def dijktra(myList,start):
    co_ordinates=dict()
    co_ordinates['A']=Point(0,0)
    myQ=[]
    heapq.heappush(myQ,(0,start))
    distance=dict()
    a=float('inf')
    for i in myList.keys():
        distance[i]=a
    distance[start]=0
    visited=set()
    parent=dict()
    parent[start]=start
    while myQ:
        current_distance,current_node=heapq.heappop(myQ)
        print(current_distance,current_node)
        if current_node in visited:
            continue
        visited.add(current_node)
        distance[current_node]=current_distance
        for neigbhours in myList[current_node]:
            neigbhours_vertext=neigbhours[0]
            neigbhours_weight=neigbhours[1]
            if distance[neigbhours_vertext]>current_distance+neigbhours_weight:
                parent[neigbhours_vertext]=current_node
                heapq.heappush(myQ,(current_distance+neigbhours_weight+heuristic(start,current_node),neigbhours_vertext))
    return distance,parent

def path(parent,cur):
    if parent[cur]==cur:
        print(cur,end=' ')
        return
    print(cur,end=' ')
    path(parent,parent[cur])
distance,parent=(dijktra(myList,'A'))
print(distance)
path(parent,'D')
