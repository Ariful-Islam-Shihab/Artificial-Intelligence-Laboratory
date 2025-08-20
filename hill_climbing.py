import random
n=int(input())
co_ordinates=[]
for i in range(n):
    co_ordinates.append(list(map(int, input().split())))


def hillClimbing(n,co_ordinates):
    def heuristic(path):
        distance=0
        for i in range(len(path)-1):
            x1,y1=co_ordinates[path[i]-1][0],co_ordinates[path[i]-1][1]
            x2,y2=co_ordinates[path[i+1]-1][0],co_ordinates[path[i+1]-1][1]
            distance+=abs(x1-x2)+abs(y1-y2)
        return distance
    def neighbour(path):
        neighbour=[]
        for i in range(len(path)):
            x=path.copy()
            x1,x2=random.randint(1,len(path)-2),random.randint(1,len(path)-2)
            x[x1],x[x2]=x[x2],x[x1]
            neighbour.append(x)
        return neighbour
    x=list(range(2,n+1))
    random.shuffle(x)
    initial_path=[1]+x+[1]
    initial_heuristic=heuristic(initial_path)
    while True:
        neighbours=neighbour(initial_path)
        min_neighbour=min(neighbours,key=heuristic)
        min_heuristic=heuristic(min_neighbour)
        if min_heuristic>initial_heuristic:
            return initial_path,initial_heuristic
        initial_path=min_neighbour
        initial_heuristic=min_heuristic




path,cost=hillClimbing(n,co_ordinates)
print(cost)
print(path)