# 2022/11/22 백트래킹
import sys
input = sys.stdin.readline

# 대상이 팀인 경우와 팀이 아닌 경우를 동시에 수행한다.
def back(t):
  # 팀 구성이 완료됐다면 search() 수행
  if t == N:
    search()
    return
  visited[t] = True
  back(t + 1)
  visited[t] = False
  back(t + 1)

# 팀 구성에 따른 점수를 계산한다.
def search():
  global res
  p1, p2 = 0, 0
  for i in range(N):
    for j in range(N):
      if visited[i] and visited[j]:
        p1 += graph[i][j]
      elif not visited[i] and not visited[j]:
        p2 += graph[i][j]
  # 작은 값을 res로 둔다
  res = min(res, abs(p1-p2))

# 정보 입력
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
res = int(1e9)

# 시작
back(0)

# 정답 출력
print(res)