# 2023/03/20 BFS
# https://www.acmicpc.net/problem/1327
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  f_list = ''.join(map(str, sorted(arr)))
  data = ''.join(map(str, arr))
  visited = set() # data 모양 저장
  visited.add(data)
  q = deque()
  q.append((data, 0))
  while q:
    d, cnt = q.popleft()
    if d == f_list: # data의 형태가 정렬된 형태인 경우 cnt 반환
      return cnt
    for i in range(N):
      if i + K <= N: # K개 만큼 뒤집을 수 있는 경우
        nd = d[:i] + d[i:i+K][::-1] + d[i+K:]
        if nd not in visited:
          visited.add(nd)
          q.append((nd, cnt + 1))
      else:
        break
  return -1 # 오름차순으로 만들 수 없는 경우 -1 반환

N, K = map(int,input().split())
arr = list(map(int,input().split()))

# 탐색 시작
res = bfs()

# 정답 출력
print(res)