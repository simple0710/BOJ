# 2023/01/06 정렬
# https://www.acmicpc.net/problem/10867
N = int(input())
print(*sorted(list(set(map(int,input().split())))))