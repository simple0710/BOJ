# 2022/11/24 조합론
import sys
input = sys.stdin.readline

# 정보 입력
N = int(input())
arr = list(map(int,input().split()))

flag = 0
# 시작
for i in range(N-1, 0, -1):
  # 왼쪽의 값이 더 큰 경우 스왑
  if arr[i-1] > arr[i]:
    for j in range(N-1, 0, -1):
      if arr[i-1] > arr[j]:
        arr[i-1], arr[j] = arr[j], arr[i-1] # 스왑
        arr = arr[:i] + sorted(arr[i:], reverse=True)
        flag = 1
        break
  # 답을 찾은 경우 정답 출력
  if flag:
    print(*arr)
    sys.exit()
# 정답을 못찾은 경우 -1 출력
if not flag:
  print(-1) 