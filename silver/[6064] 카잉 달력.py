def num(m, n, x, y):
    # x에 m을 더한 값을 n으로 나눈다.
    while x <= m * n:
        # 나누어 지면 x를 return
        if (x - y) % n == 0:
           return x
        # 그렇지 않으면 x += m
        x += m
    # x가 m * n보다 크다면 -1
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
