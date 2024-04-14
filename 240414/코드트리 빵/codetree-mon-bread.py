'''
1. 최단거리 문제 bfs로 관리
2. 상우좌하로 움직임
3. 모두 움직이고 그 다음


변수 처리
graph : 내가 움지일 수 있는 경로 담는 0,1,2 >> list(list)
stores_graph : 사람들이 원하는 스토어 위치 담는 그래프 >> list(tuple)
people : 사람들 상태표시 >> list

bfs
visited : 방문기록 표시 >> list
step : 갈 수 있는 가장 최단거리 step 표시


cur_time : 현재 시간 기록용
n, m : n 지도 크기, 사람수

'''

from collections import deque

EMPTY = (-1,-1)

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
stores_graph = []

for _ in range(m):
    a,b = map(int, input().split())
    stores_graph.append((a-1,b-1))


# 현재 시간 기록용
curr_time = 0

# 커서 우선 순위 상좌우하임
dx = [-1,0,0,1]
dy = [0,-1,1,0]

# bfs용
visited = [[False]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]

people = [EMPTY]*m
# # print('start')
# print(people)

# # 격자내에 있는 곳인지 판단

def move_in(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# # 이동 가능한 곳인지 판단 1. 격자 안 2. 방문한적 아님 2. 이동가능한 곳
def move_ok(x, y):
    return move_in(x,y) and not visited[x][y] and graph[x][y] != 2 


# # bfs 시작 -> 최단거리 계산
# # 시작점이 계속 바뀜 0에서 시작임 아님 왜냐면 시뮬레이션으로 진행되어야함
# # 원래같은면 그냥 방문 기록을 유지하면서 0,0이나 시작점으로 넣어주면 되는데 여기는 초기화하는거 때문인지

def bfs(start_pos):
    # 초기화 작업 먼저 시행
    # why : 가장 최적의 거리 찾기 위해서 1타임에 여러 안을 빼내야해서 초기화 시키고 진행해야함
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    q = deque()
    sx, sy = start_pos
    q.append(start_pos)
    visited[sx][sy] =True
    step[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if move_ok(nx,ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx,ny))

        
# 시뮬레이션
def simulate():
    # step1. 격자에 있는 사람들은 편의점 방향으로 향해 1칸씩 움직임 (격자에 있다는건 이미 자기 움직일 수 있는 시간이 지났다는거)
    for i in range(m):
        # 만약에 사람이 격자내에 없거나, 이미 편의점에 들어가있으면 안움직임
        if people[i] == EMPTY or people[i] == stores_graph[i]:
            continue

        bfs(stores_graph[i])
        
        px, py = people[i]
        dist_min = 1e5
        min_x,min_y = -1,-1
        for j in range(4):
            nx = px + dx[j]
            ny = py + dy[j]
            
            # 방문에서 1이어여하고 dist 보다 step이 작아야하고 안쪽에 있어야함
            if move_ok(nx,ny) and visited[nx][ny] and dist_min > step[nx][ny]:
                dist_min = step[nx][ny]
                min_x,min_y = nx,ny 
        
        people[i] = (min_x,min_y)
        


    # step2. 편의점 도착한 사람들 2표시 앞으로 이동 불가
    for k in range(m):
        if people[k] == stores_graph[k]:
            px, py = people[k]
            graph[px][py] = 2


    # step3. 현재 시간에 t 사람이 베이스 캠프로 이동

    if curr_time > m:
        return

    bfs(stores_graph[curr_time-1])

    dist_min = 1e5
    min_x,min_y = -1,-1

    for i in range(n):
        for j in range(n):
            if visited[i][j] and graph[i][j] == 1 and dist_min > step[i][j]:
                dist_min = step[i][j]
                min_x,min_y = i,j

    people[curr_time-1] = (min_x,min_y)
    graph[min_x][min_y] = 2




# # 편의점 도착했는지 파악
def end():
    for i in range(m):
        if people[i] != stores_graph[i]:
            return False
        
    return True



# # 1분에 한번씩 시뮬레이션 돌리기
while True:
    curr_time += 1
    simulate()
    if end():
        break

print(curr_time)