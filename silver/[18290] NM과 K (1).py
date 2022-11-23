# 2022/11/23 백트래킹
# 
# 2 2 2
# -1 -2
# -3 -5
# 위의 경우 depth가 K인 경우에 방문 기록을 확인하면
# if x == now_x가 없으면 하나밖에 나오지 않는다.

def back(now_x, now_y, depth, sum):
  global res
  # 깊이가 K와 같은 경우 res와 sum을 비교한 후 종료
  if depth == K:
    res = max(res, sum)
    return

  # 자신의 위치부터 전 지역 탐색
  for x in range(now_x, N):
    # 모든 부분을 탐색하기 위해 if x == now_x를 사용한다.
    for y in range(now_y if x == now_x else 0, M):
      if x == now_x:
        print(y)
      # 이미 방문했으면 continue
      if visited[x][y]:
        continue
      flag = True
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
          # 인접한 지역이 방문했다면 False
          if visited[nx][ny]:
            flag = False
      # 인접한 지역을 방문하지 않았다면 재귀 수행
      if flag:
        visited[x][y] = True
        back(x, y, depth+1, sum+arr[x][y])
        visited[x][y] = False

# 정보 입력
N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = -int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백트래킹 시작
back(0, 0, 0, 0)

# 정답 출력
print(res)