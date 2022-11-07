# 2022/10/29 백트래킹
import sys
input = sys.stdin.readline

def back(start, next, value, visited):
  global res
  # 방문이 전부 완료 됐을 경우
  if len(visited) == N:
    # 출발지로 갈 수 있는 길이 있는 경우
    if data[next][start] != 0:
      # 현재 값 vs 새로 계산된 값
      res = min(res, value + data[next][start])
    return
  
  for i in range(N):
    # 갈 수 있는 길이고, i가 시작지점으로 가는게 아니고, 방문하지 않은 경우 back
    if data[next][i] != 0 and i != start and i not in visited:
      visited.append(i)
      back(start, i, value + data[next][i], visited)
      visited.pop()

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
res = sys.maxsize
print(res)

# 수행
for i in range(N):
  back(i, i, 0, [i])

# 출력
print(res)