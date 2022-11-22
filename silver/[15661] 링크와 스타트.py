# 2022/11/22 백트래킹
import sys
input = sys.stdin.readline

# 백트래킹
def back(depth, idx, finish):
  global res
  # 깊이가 finish와 같은 경우
  if depth == finish:
    p1, p2 = 0, 0
    for i in range(N):
      for j in range(N):
        # 해당 번호와 같은 팀인 경우 p에 점수를 추가한다.
        if visited[i] and visited[j]:
          p1 += graph[i][j]
        elif not visited[i] and not visited[j]:
          p2 += graph[i][j]
    # res와 값을 비교해 낮은 값을 res로 한다.
    res = min(res, abs(p1-p2))
    return
  # idx부터 시작
  for i in range(idx, N):
    if not visited[i]:
      visited[i] = True
      back(depth+1, i+1 ,finish)
      visited[i] = False

# 정보 입력
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
res = int(1e9)

# 백트래킹 시작
for x in range(N):
  back(0, 0, x)

# 정답 출력
print(res)