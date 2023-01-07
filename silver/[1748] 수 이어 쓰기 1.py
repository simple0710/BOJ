# 2023/01/01 구현
# https://www.acmicpc.net/problem/1748
import sys
input = sys.stdin.readline

N = input()
len_N = len(N) - 1
answer = 0
# 해당 자리수의 최대 자리수의 합 구하기
for i in range(len_N):
  answer +=  9 * (10 ** i) * (i + 1)

answer += ((int(N) - (10 ** len_N)) + 1 ) * (len_N * 1)

# 정답 출력
print(answer)