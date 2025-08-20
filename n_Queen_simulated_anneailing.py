import copy
import random
import math
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
start=(0,0)
# n=8
# board=[
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0]
# ]
def simulated_anneailing(board):
    def positions(board):
        pos = []
        for i in range(n):
            for j in range(n):
                if board[j][i] == 1:
                    pos.append((j, i))
        return pos
    def heuristic(board):
        pos=positions(board)
        h=0
        for i in pos:
            for j in pos:
                if i!=j:
                    y=abs(i[0]-j[0])
                    x=abs(i[1]-j[1])
                    if x==0:
                        h+=1
                        continue
                    rate=y/x
                    if rate==1 or rate==-1 or rate==0:
                        h+=1
        return h/2
    def get_neigbours(j):
        neighbours=[]
        for i in range(n):
            neighbours.append((i,j))
        return neighbours
    i=0
    j=0
    T=100
    cooling_rate=0.85
    current=copy.deepcopy(board)
    path=[]
    while i<=100:
        if heuristic(current)==0:
            path.append(copy.deepcopy(current))
            return True,path
        path.append(copy.deepcopy(current))
        neighbours=get_neigbours(j)
        pos=positions(current)
        # print(pos)
        # print()
        neighbours.remove(pos[j])
        best_neighbour=random.choice(neighbours)
        new_board=copy.deepcopy(current)
        new_board[pos[j][0]][pos[j][1]]=0
        new_board[best_neighbour[0]][best_neighbour[1]]=1
        best_heuristic=heuristic(new_board)
        # for neighbour in neighbours:
        #     new_board=copy.deepcopy(current)

        #     new_board[pos[j][0]][pos[j][1]]=0
        #     new_board[neighbour[0]][neighbour[1]]=1
        #     h=heuristic(new_board)
        #     if h<best_heuristic:
        #         best_heuristic=h
        #         best_neighbour=neighbour
        if best_heuristic>heuristic(current):
            delta=heuristic(current)-best_heuristic
            probability=math.exp(delta/T)
            rmg=random.uniform(0,1)
            if rmg>probability:
                # path.append(copy.deepcopy(current))
                print("Not accepted")
                return False,path
        current=new_board
        T=T*cooling_rate
        if T < 1e-10:
            break
        j=(j+1)%n
        i+=1
    return False,path
result,path=simulated_anneailing(board)
if result:
    print("Solution found")

    # print(path)
else:
    print("No solution found")
    # print(len(path))
    # print(path)
for idx, step in enumerate(path):
    print(f"Step {idx}:")
    for row in step:
        print(row)
    print()
