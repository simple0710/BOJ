# 2022/11/22 백트래킹
import sys
input = sys.stdin.readline

# 백트래킹
def back(depth, idx):
  global res
  # 깊이가 N의 절반인 경우
  if depth == N//2:
    p1, p2 = 0, 0
    for i in range(N):
      for j in range(N):
        # 해당 번호가 같은 팀인 경우 p1에 점수를 추가한다.
        if visited[i] and visited[j]:
          p1 += data[i][j]
        # 해당 번호가 같은 팀인 경우 p2에 점수를 추가한다.
        elif not visited[i] and not visited[j]:
          p2 += data[i][j]
    # res와 값을 비교해 낮은 값을 res로 한다.
    res = min(res, abs(p1-p2))
    return
  # idx부터 시작
  for i in range(idx, N):
    # 방문하지 않다면 True후 depth+1, idx+1을 수행 후 다시 False를 한다.
    if not visited[i]:
      visited[i] = True
      back(depth+1, i + 1)
      visited[i] = False

# 정보 입력
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
res = int(1e9)

# 백트래킹 시작
back(0, 0)

# 정답 출력
print(res)