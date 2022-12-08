# 2022/12/01 구현
# https://www.acmicpc.net/problem/16931
N, M = map(int,input().split())
tower = [list(map(int,input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
squre_area = 0
# 전 범위 탐색
for i in range(N):
   for j in range(M):
    # 6, 10, 14, 18...
    tmp = 6 + (tower[i][j]-1) * 4
    # 주변 탐색
    for x in range(4):
      nx = i + dx[x]
      ny = j + dy[x]
      if 0 <= nx < N and 0 <= ny < M:
        # 만약 현재 위치보다 비교 위치가 더 크다면 자신의 크기만큼 뺀다.
        if tower[nx][ny] >= tower[i][j]:
          tmp -= tower[i][j]
        # 만약 비교 위치보다 현재 위치가 더 크다면 
        else:
          tmp -= tower[nx][ny]
    # 정답에 추가
    squre_area += tmp
# 정답 출력
print(squre_area)