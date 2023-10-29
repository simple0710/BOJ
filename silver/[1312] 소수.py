# 2023/07/17 Math
# https://www.acmicpc.net/problem/1312
A, B, N = map(int,input().split())
for _ in range(N): # N번 반복
  A = (A % B) * 10
# 정답 출력
print(A//B)