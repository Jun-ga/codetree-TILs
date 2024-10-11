from collections import deque
import copy

def rotate(arr,x,y,n): # 돌리기
    new = copy.deepcopy(arr)
    temp_arr = [[0]*3 for _ in range(3)]
    new_arr = [[0]*3 for _ in range(3)]

    start_x, start_y = x-1,y-1

    for i in range(3):
        for j in range(3):
            temp_arr[i][j] = arr[start_x+i][start_y+j]
    if n == 90:
        for i in range(3):
            for j in range(3):
                new_arr[j][3-1-i] = temp_arr[i][j]
    elif n == 180:
        for i in range(3):
            for j in range(3):
                new_arr[3-1-i][3-1-j] = temp_arr[i][j]
    elif n == 270:
        for i in range(3):
            for j in range(3):
                new_arr[3-1-j][i] = temp_arr[i][j]
    for i in range(3):
        for j in range(3):
            new[start_x+i][start_y+j] = new_arr[i][j]

    return new


def bfs_check(MAP,clr):

    visit = [[0] * 5 for _ in range(5)]
    point = 0

    for i in range(5):
        for j in range(5):
            if visit[i][j] == 0:
                term = bfs(i,j, MAP,visit,clr)
                point += term


    return point

def bfs(i,j,MAP,visit, clr):
    node = []
    count = 0


    bfs_deque = deque()
    bfs_deque.append((i,j))
    node.append((i,j))
    visit[i][j] = 1
    count +=1

    while bfs_deque:
        x,y = bfs_deque.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 5 and 0<= ny < 5 and  MAP[x][y] == MAP[nx][ny] and visit[nx][ny] == 0:
                count += 1
                visit[nx][ny] = 1
                bfs_deque.append((nx, ny))
                node.append((nx,ny))

    if count >= 3:
        if clr == 1 :
            for I, J in node:
                MAP[I][J] = 0
        return count
    else:
        return 0



K, M = map(int, input().split())
MAP = [] # 유물
for _ in range(5):
    MAP.append(list(map(int, input().split())))
item_num = list(map(int, input().split())) #새로 생기는 유물

dx = [-1,1, 0, 0]
dy = [0,0,-1,1]

answer = []

for _ in range(K): #K 만큼 반복할거임 탐사를
    # [1]
    max_point = 0

    # 가능한 모든 중점과 각을 확인한 후 가장 좋은 값 나옴
    for n in (90,180,270):
        for y in range(1,4):
            for x in range(1,4):
                new_MAP = rotate(MAP, x, y, n)


                ans = bfs_check(new_MAP,0)
                if max_point < ans:
                    max_point = ans
                    MMAP = new_MAP



    if max_point == 0: # 할 값이 없는 상황임
        break

    # [2] 연쇄 획득
    point = 0
    MAP = MMAP
    while True:
        count =  bfs_check(MAP, 1)
        if count == 0:
            break
        point += count

        for j in range(5):
            for i in range(4,-1,-1):
                if MAP[i][j] == 0:
                    MAP[i][j] = item_num.pop(0)

    answer.append(point)

print(*answer)