# 2023/06/18 Implementation, Simulation, Sorting
# https://www.acmicpc.net/problem/17140
# 3 x 3 배열 A
# R 연산 : 모든 행 정렬, 행 >= 열
# C 연산 : 모든 열 정렬, 행 < 열

# 오름차순 정렬 1. 수의 등장 횟수가 커지는 순, 2. 수가 커지는 순
# 크기가 커진 곳엔 0이 채워진다.
# 정렬시에 0은 무시한다.
# 열 또는 행의 길이는 100으로 제한한다.

# A[r][c]의 값이 k가 되기 위한 최소 시간을 구한다
# 100초가 지나도 안되면 -1 출력
def cal(arr, x, y, flag):
  max_length = 0
  new_arr_check = []
  for i in arr:
    check_data = []
    check_number = set([0])
    # 등장 횟수 구하기
    for j in set(list(i)):
      if j not in check_number:
        check_number.add(j)
        number_cnt = i.count(j)
        check_data.append((j, number_cnt))
    max_length = max(max_length, len(check_data) * 2)
    # 1. 수의 등장 횟수 오름차 정렬
    # 2. 수의 크기 오름차 정렬
    check_data.sort(key=lambda x: (x[1], x[0]))
    new_data = []
    for a, b in check_data:
      new_data += [a, b]
    new_arr_check.append(new_data)
  new_arr = []
  for i in new_arr_check: # 빈 공간에 0 채우기
    new_arr.append(i + [0] * (max_length - len(i)))
  if flag: # C 연산을 수행한 경우
    new_arr = [list(i) for i in zip(*new_arr)]
    solution(new_arr, max_length, y)
  else: # R 연산을 수행한 경우
    solution(new_arr, x, max_length)

def solution(arr, x_length, y_length):
  global res
  if res > 100: # 100을 초과한 경우 -1출력 후 종료
    print(-1)
    exit(0)
  # 행, 열의 크기 제한은 각각 100으로 한다.
  if x_length >= 100:
    arr = arr[:100]
  if y_length >= 100:
    arr =[i[:100] for i in arr]
  if x_length >= R and y_length >= C: # 탐색할 위치 R, C를 탐색할 수 있는 경우
    if arr[R-1][C-1] == K: # 해당 위치 확인 후 K와 같으면 res 출력
      print(res)
      exit(0)
  res += 1
  if x_length >= y_length: # R 연산
    cal(arr, x_length, y_length, False)
  else: # C 연산
    cal(zip(*arr), x_length, y_length, True)

R, C, K = map(int,input().split())
arr = []
for _ in range(3):
  arr.append(list(map(int,input().split())))

res = 0
# 탐색 시작
solution(arr, 3, 3)