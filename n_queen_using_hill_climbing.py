import copy
n=int(input())
print(n)
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
def hill_climbing(board):
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
    max_iterations=100
    current=copy.deepcopy(board)
    path=[]
    while True:
        if heuristic(current)==0:
            path.append(copy.deepcopy(current))
            return True,path
        path.append(copy.deepcopy(current))
        neighbours=get_neigbours(j)
        pos=positions(current)
        # print(pos)
        # print()
        neighbours.remove(pos[j])
        best_neighbour=None
        best_heuristic=float('inf')
        for neighbour in neighbours:
            new_board=copy.deepcopy(current)

            new_board[pos[j][0]][pos[j][1]]=0
            new_board[neighbour[0]][neighbour[1]]=1
            h=heuristic(new_board)
            if h<best_heuristic:
                best_heuristic=h
                best_neighbour=neighbour
        if best_heuristic>heuristic(current) and j==n-1:
            # path.append(copy.deepcopy(current))
            return False,path
        current[pos[j][0]][pos[j][1]]=0
        current[best_neighbour[0]][best_neighbour[1]]=1
        # print(current)
        j=(j+1)%n
        i+=1
    return False,path
result,path=hill_climbing(board)
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
