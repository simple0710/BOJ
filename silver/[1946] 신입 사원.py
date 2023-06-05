# 2023/06/04 Greedy, Sorting
# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  data = []
  for _ in range(N):
    data.append(list(map(int,input().split())))
  data.sort(key=lambda x: x[0]) # 서류심사 성적 오름차 정렬
  max_b = data[0][1]
  res = 0
  for x, y in data:
    if y <= max_b: # 면접 성적 비교
      res += 1
      max_b = y
  # 정답 출력
  print(res)

