import sys

input = sys.stdin.readline

def fibonacci(n):
    # 3을 길이로 지정한다.
    length = len(zero)
    # 만약 3보다 n이 크다면 반복문 실행 
    if n >= length:
        # 각 -1번째와 -2번째의 수를 합한 값을 추가한다.
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

t = int(input())
# 0이 호출되는 수는 1, 0, 1, 1, 1 ,2, 3 순으로 진행된다.
zero = [1, 0, 1]
# 1이 호출되는 수는 0, 1, 1, 2, 3, 5, 8 순으로 진행된다.
one = [0, 1, 1]

for _ in range(t):
    a = int(input())
    fibonacci(a)
