# 2023/03/12 Ad-Hoc
# https://www.acmicpc.net/problem/27738
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
res = 0
# 시작 지점은 arr[5]의 배수 부터 시작한다.
# arr[5]의 배수인 경우 0이 되기 때문이다.
for i in range(arr[5] * (N // arr[5]) + 1, N + 1):
  if i % arr[0] == 0:
    res += i
  if i % arr[1] == 0:
    res %= i
  if i % arr[2] == 0:
    res &= i
  if i % arr[3] == 0:
    res ^= i
  if i % arr[4] == 0:
    res |= i
# 정답 출력
print(res)