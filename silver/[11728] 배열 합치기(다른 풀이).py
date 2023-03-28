# 2023/03/28 Two Pointer
# https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
res = []
a, b = 0, 0
while a != len(A) or b != len(B): # 탐색 시작
    if a == len(A): # a가 끝까지 도착한 경우
      res.append(B[b])
      b += 1
    elif b == len(B): # b가 끝까지 도착한 경우
      res.append(A[a])
      a += 1
    else:
      # 각각의 값을 비교한다.
      if A[a] < B[b]:
        res.append(A[a])
        a += 1
      else:
        res.append(B[b])
        b += 1
# 정답 출력
print(*res)