# 2023/01/05 자료 구조
# https://www.acmicpc.net/problem/1158
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
K -= 1 # 해당 칸을 지우고 이동하므로 -1을 한다.
arr = [i for i in range(1, N + 1)]
res = []
start = K
# 해당 칸을 지우고 len(arr)를 넘은 경우 start를 나머지 값으로 한다.
while arr:
  start %= len(arr)
  res.append(arr[start])
  del arr[start]
  start += K

# 정답 출력
print('<' + ', '.join(map(str, res)) + '>')