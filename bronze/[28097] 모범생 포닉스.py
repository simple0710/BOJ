# 2023/06/26 Math
# https://www.acmicpc.net/problem/28097
N = int(input())
# 공부 시간 + 휴식 시간
data = sum(list(map(int,input().split()))) + (N - 1) * 8
# 정답 출력(a일, b시간)
print(data // 24, data % 24)