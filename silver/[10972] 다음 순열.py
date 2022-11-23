# 2022/11/23 조합론
import sys
input = sys.stdin.readline

# 정보 입력
n = int(input())
arr = list(map(int,input().split()))
find = False

# 뒤에서부터 전체를 탐색한다.
for i in range(n-1, 0, -1):
  # 뒤의 값이 더 큰 경우
  if arr[i-1] < arr[i]:
    for j in range(n-1, 0, -1):
      if arr[i-1] < arr[j]:
        arr[i-1], arr[j] = arr[j], arr[i-1] # 스왑
        arr = arr[:i] + sorted(arr[i:])
        find = True
        break
  # 찾은 경우 정답 출력
  if find:
    print(*arr)
    break
# 못 찾은 경우 -1 출력
if not find:
  print(-1)