import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어난 경우
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        # 배추를 심지 않은 땅인 경우
        if data[ny][nx] == 0:
            continue
        data[ny][nx] = 0
        dfs(nx, ny)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split())
    data = list()
    for i in range(n):
        data.append([0]*m)
    cnt = 0
    # 배추 위치를 입력 받음
    for _ in range(k):
        x, y = map(int,input().split())
        data[y][x] = 1
    # 전 지역에 대해 한 번씩 확인
    for x in range(m):
        for y in range(n):
            if data[y][x] == 1:
                dfs(x,y)
                cnt += 1
    print(cnt)