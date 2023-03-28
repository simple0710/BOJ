# 2023/03/28 Implementation
# https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 정답 출력
print(*sorted(A + B))