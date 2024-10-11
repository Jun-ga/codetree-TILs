'''
1)아래가 우선순위
2)그다음이 서쪽 반시계 방향 회전
3) 동쪽 시계방향

예외처리
만약 골렘이 들어가지 못하는 상황이면
그 친구를 빼고 한번 돌고 다음에 다시 진행

bfs로 하단 까지 내려가는 최단거리 (남쪽으로 가는 가장 최단 거리를 찾아야함)
출구가 있으면 다른 골렘으로 이동이 가능함

'''
from collections import deque

n,m,K = map(int, input().split())
graph = [[0]*m for _ in range(n)]
ans = 0
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def Exit(x,y,d):
    if d == 0:
        return [x-1, y]
    elif d==1:
        return [x,y+1]
    elif d==2:
        return [x+1,y]
    else:
        return [x,y-1]

def inBoard(nx,ny):
    if 0 <= nx < n and 0 <= ny < m :
        return True
    return False

def check(x,y): # check
    if not inBoard(x,y):
        if x<n and 0<=y<m:
            return True
    else : # 좌표내 가능
        if graph[x][y] == 0:
            return True
    return False


def move(c,d,num):
    global graph

    x,y = -2, c-1 # 처음 시작

    while True:
        if check(x+2,y) and check(x+1,y-1) and check(x+1,y+1):
            x+=1
        elif check(x+1,y-1) and check(x-1,y-1) and check(x,y-2) and check(x+1,y-2) and check(x+2,y-1):
            x+=1
            y-=1
            d=(d-1)%4
        # 골렘 오른쪽 이동
        elif check(x+1,y+1) and check(x-1,y+1) and check(x,y+2) and check(x+1,y+2) and check(x+2,y+1):
            x+=1
            y+=1
            d=(d+1)%4
        else:
            break

    if not inBoard(x, y) or not inBoard(x + 1, y) or not inBoard(x-1,y) or not inBoard(x,y+1) or not inBoard(x,y-1):
        return [False, -1, -1]
    else:
        graph[x][y] = graph[x-1][y] = graph[x+1][y]= graph[x][y+1] = graph[x][y-1] = num
        ex, ey = Exit(x,y,d)
        graph[ex][ey] = -num

        return [True, x, y]

def bfs(sx,sy,num):
    #global ans
    cand = []
    bfs_deque = deque()
    bfs_deque.append((sx,sy))
    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] =True

    while bfs_deque:
        x,y = bfs_deque.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not inBoard(nx,ny) or visited[nx][ny] or graph[nx][ny] == 0:
                continue
            if abs(graph[x][y]) == abs(graph[nx][ny]) or graph[x][y] < 0  and abs(graph[nx][ny] != abs(graph[x][y])):
                bfs_deque.append((nx,ny))
                visited[nx][ny] = True
                cand.append(nx)

    cand.sort(reverse=True)
    point = cand[0]+1
    return point

for num in range(1,K+1):
    c,d = map(int, input().split())

    res = move(c,d,num)
    inBoards, x, y = res

    if inBoards :
        ans += bfs(x,y,num)
    else:
        graph = [[0]*m for _ in range(n)]

print(ans)