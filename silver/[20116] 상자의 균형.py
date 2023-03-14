# 2023/03/14 PrefixSum
# https://www.acmicpc.net/problem/20116
N, L = map(int,input().split())
arr = list(map(int,input().split()))

# 누적합으로 값을 저장해 둔다.
data = [0] * N
for i in range(1, N):
  data[i] = data[i-1] + arr[i]

flag = True
for i in range(N-1):
  now_box = arr[i]
  next_box = arr[i+1]
  areaL = now_box - L
  areaR = now_box + L
  # 다음 박스의 위치가 현재 박스 위치 안에 있는 경우
  if areaL < next_box-L < areaR or areaL < next_box+L < areaR or areaL < next_box < areaR:
    # 무게 중심이 벗어난 경우
    if not areaL < (data[-1] - data[i]) / (N - 1 - i) < areaR:
      flag = False
      break
  # 박스의 위치가 벗어난 경우
  else:
    flag = False
    break
# 정답 출력
if flag:
  print("stable")
else:
  print("unstable")