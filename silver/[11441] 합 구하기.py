import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
# 누적 합을 적용한다
for i in range(1, len(data)):
  data[i] += data[i-1]

t = int(input())
for i in range(t):
  # 범위를 지정 받는다.
  x, y = map(int,input().split())
  # 만약 x가 1이면 data[y-1]을 출력한다.
  if x == 1:
    print(data[y-1])
  # x-2인 이유는 x = 2인 경우 -1을 해야 인덱스를 맞추고 그 이전 값을
  # 빼야 합이 나오기 때문이다
  else:
    print(data[y-1]-data[x-2])
