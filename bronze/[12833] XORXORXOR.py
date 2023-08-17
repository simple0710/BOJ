# 2023/06/29 Math, Bitmasking
# https://www.acmicpc.net/problem/12833
# N번째 결과는 N + 2결과와 같다.
A, B, C=map(int, input().split())
for i in range(C%2):
  A^=B
# 정답 출력
print(A)