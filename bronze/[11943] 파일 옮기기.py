# 2023/07/01 Math, Implementation
# https://www.acmicpc.net/problem/11943
A, B = map(int,input().split())
C, D = map(int,input().split())
# 최소 이동 횟수 출력
print(min(A+D, C+B))