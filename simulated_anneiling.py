import random
import math
n=int(input())
co_ordinates=[]
for i in range(n):
    co_ordinates.append(list(map(int, input().split())))


def hillClimbing(n,co_ordinates,T,cooling_rate):
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
        selected=random.choice(neighbours)
        selected_heuristic=heuristic(selected)
        if selected_heuristic>initial_heuristic:
            delta=selected_heuristic-initial_heuristic
            probability=math.exp((delta/T)*-1)
            rmg=random.uniform(0,1)
            if rmg<=probability:
                initial_path=selected
                initial_heuristic=selected_heuristic
            else:
                print("probability",probability)
                return initial_path,initial_heuristic
        
        initial_path=selected
        initial_heuristic=selected_heuristic
        T=T*cooling_rate
        if T<0.1:
            print("T<0.1")
            return initial_path,initial_heuristic




path,cost=hillClimbing(n,co_ordinates,100,0.95)
print(cost)
print(path)