# 2023/03/27 Implementation
# https://www.acmicpc.net/problem/18422
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
data = [(list(input().rstrip()) +['.']) for _ in range(N)]
data.append(['.'] * M)
res = 0
for i in range(N):
  for j in range(M):
    if data[i][j] == '*' and data[i+1][j] == data[i][j+1] == '.': # 오른쪽 하단 개수 구하기
      res += 1
# 정답 출력
print(res)