# 2023/06/30 Math, Implementaion
# https://www.acmicpc.net/problem/28281
import sys
MAX = sys.maxsize

N, X = map(int, input().split())
data = list(map(int,input().split()))
res = MAX
for i in range(1, N):
  # 연속된 날짜에 대해 양말 구입 비교
  res = min(res, data[i-1] * X + data[i] * X)
# 정답 출력
print(res)