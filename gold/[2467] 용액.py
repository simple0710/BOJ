# 2022/11/19 두 포인터, 이분 탐색
import sys
input = sys.stdin.readline

# 정보 입력
N = int(input())
arr = list(map(int,input().split()))

# 시작 위치 지정
start = 0
end = N - 1

# 정답 x, y 정의 및 res 정의
res = sys.maxsize
x = 0
y = 0
while start < end:
  check = arr[start] + arr[end]
  # check이 res보다 작다면 값 수정 및 x, y 재정의
  if abs(check) <= res:
    res = abs(check)
    x = start
    y = end
  # check가 양수인 경우 end -= 1
  if check > 0:
    end -= 1
  # check가 음수인 경우 start += 1
  elif check < 0:
    start += 1
  # check가 0인 경우 종류
  else:
    break

# 정답 출력
print(arr[x], arr[y])