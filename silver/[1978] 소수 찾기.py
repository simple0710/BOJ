import sys
input = sys.stdin.readline

n =  input()
data = map(int,input().split())

cnt = 0
check = 0
for i in data:
    if i == 1:
        continue
    if i == 2:
        cnt += 1
    # 2 ~ i 까지 수를 비교해서 나눠지면 소수 x
    for j in range(2, i):
        if i % j == 0:
            check = 0
            break
        check = 1
    cnt += check
print(cnt)
