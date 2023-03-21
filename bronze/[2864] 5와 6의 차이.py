# 2023/03/21 Implementation
# https://www.acmicpc.net/problem/2864
num = input().split()
a = num[0].replace('5', '6')
b = num[1].replace('5', '6')
ma = int(a) + int(b) # 최댓값
a = num[0].replace('6', '5')
b = num[1].replace('6', '5')
mi = int(a) + int(b) # 최솟값
# 정답 출력
print(mi, ma)
