# 2023/01/26 문자열, 정렬
# https://www.acmicpc.net/problem/5635
import sys
input = sys.stdin.readline

data = []
for _ in range(int(input())):
  n, d, m, y = input().rstrip().split()
  d, m, y = map(int,(d, m, y)) # int값으로 변경
  data.append((y, m, d, n)) # 연, 월, 일, 이름 순으로 저장한다.
data.sort() # 정렬
# 정답 출력
print(data[-1][3])
print(data[0][3])