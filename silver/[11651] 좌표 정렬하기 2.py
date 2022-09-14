import sys
input = sys.stdin.readline

n = int(input())
data = list()
# 데이터를 입력 받는다
for i in range(n):
    x, y = map(int,input().split())
    data.append((x,y))
# x를 기준으로 한번 정렬하고 y를 기준으로 정렬한다
data = sorted(data, key = lambda x:x[0])
data = sorted(data, key = lambda x:x[1])

# 출력
for i in range(n):
    for j in range(2):
        print(data[i][j], end = ' ')
    print()
'''
data.append((y,x))로 해서
data.sort()
print(x,y)를 출력하는 방법이 있다.
'''
