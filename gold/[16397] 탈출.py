# 2023/07/23 BFS
# https://www.acmicpc.net/problem/16397
# 버튼 A : N이 1 증가
# 버튼 B : M * 2 후에 0이 아닌 가장 높은 자릿수의 숫자가 1이 줄어듦
# N이 99,999를 넘으면 실패
# B를 눌렀을 때, 99,999를 넘으면 실패
# 목표 : 최대 T회, N을 G로 만들기
from collections import deque

def bfs():
  q = deque([(N)])
  visited = [-1] * 100000
  visited[N] = 0
  while q:
    now = q.popleft()
    if visited[now] > T: # 횟수 초과
      return 'ANG'
    if now == G: # G를 만든 경우 횟수 반환
      return visited[now]
    check = [now + 1] # 버튼 A
    if now * 2 < 100000: # now * 2가 100000을 넘지 않는 경우 케이스에 추가
      # 버튼 B(N * 2 - (10 ** len(now * 2) - 1))
      check.append(now * 2 - 10 ** (len(str(now * 2)) - 1))
    for next in (check):
      if 0 <= next < 100000 and visited[next] == -1:
        visited[next] = visited[now] + 1
        q.append(next)
  # 불가능
  return "ANG"
N, T, G = map(int,input().split())
# 탐색 및 정답 출력
print(bfs())