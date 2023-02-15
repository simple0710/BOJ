# 2023/02/15 Greedy
# https://www.acmicpc.net/problem/20044
import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split()))) # 정렬

ans = sys.maxsize
while arr: # 양쪽 끝의 합을 계속 더한 후 최소 값을 구한다.
  s = arr.pop(0)
  e = arr.pop()
  ans = min(ans, s + e)

# 정답 출력
print(ans)