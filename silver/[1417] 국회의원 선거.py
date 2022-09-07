import sys
input = sys.stdin.readline

data = list()
n = int(input())
for i in range(n):
    data.append(int(input()))
# 기호 1번은 따로 분류해둔다.
my_data = data[0]
del data[0]

cnt = 0
while True:
    # 후보가 한명이면 경쟁자는 없다.
    if n == 1:
        break
    # 기호 1번이 가장 큰 수인 경우 종료
    if my_data > max(data):
        break
    # data에서 가장 큰 값을 -1하고, my_data에 +1을 한다.
    data[data.index(max(data))] -= 1
    my_data += 1
    cnt += 1
print(cnt)
