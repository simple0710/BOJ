# 2023/12/19 Implementation, Simulation
# https://www.acmicpc.net/problem/20327
import sys
input = sys.stdin.readline

# 부분 배열 연산
def spin_arr_1(k, l, x, y):
  global arr, new_arr
  x_max = x+2**l
  y_max = y+2**l
  if k == 1: # 각 부분 배열을 상하 반전시키는 연산
    for i in range(x, x_max):
      new_arr[i][y:y_max] = arr[x+(x_max-1)-i][y:y_max]
  elif k == 2: # 각 부분 배열을 좌우 반전시키는 연산
    for i in range(x, x_max):
      new_arr[i][y:y_max] = arr[i][y:y_max][::-1]
  elif k == 3: # 각 부분 배열을 오른쪽으로 90도 회전시키는 연산
    for i in range(2**l):
      for j in range(2**l):
        new_arr[x+i][y+j] = arr[x+(2**l-1)-j][y+i]
  elif k == 4: # 각 부분 배열을 왼쪽으로 90도 회전시키는 연산
    for i in range(2**l):
      for j in range(2**l):
        new_arr[x+i][y+j] = arr[x+j][y+(2**l-1)-i]

# 부분 배열을 한칸으로 처리하는 연산
def spin_arr_2(k, l, x, y):
  global arr
  x_max = x+2**l
  y_max = y+2**l
  if k == 5: # 배열을 상하 반전시키는 연산
    point = 2**N - (x_max)
    for i in range(x, x_max):
      new_arr[i][y:y_max] = arr[point+i-x][y:y_max][:]
  elif k == 6: # 좌우 반전시키는 연산
    if y >= 2**N//2: return
    for i in range(x, x_max):
      new_arr[i][y:y_max] = arr[i][2**N-y_max:2**N-y]
      new_arr[i][2**N-y_max:2**N-y] = arr[i][y:y_max]
  elif k == 7: # 배열을 오른쪽으로 90도 회전시키는 연산
    a, b = 2**N-1-y, x
    a -= a % 2**l
    for i in range(2**l):
      for j in range(2**l):
        new_arr[x+i][y+j] = arr[a+i][b+j]
  elif k == 8: # 왼쪽으로 90도 회전시키는 연산
    a, b = y, 2**N-1-x
    b -= b % 2**l
    for i in range(2**l):
      for j in range(2**l):
        new_arr[x+i][y+j] = arr[a+i][b+j]

def solution():
  global arr, new_arr
  for k, l in commands:
    new_arr = [[[] for _ in range(2**N)] for _ in range(2**N)]
    # 각각의 부분 배열에 해당하는 지점부터 연산 시작
    for x in range(0, 2**N, 2**l):
      for y in range(0, 2**N, 2**l):
        # 부분 배열 연산
        if k <= 4: spin_arr_1(k, l, x, y)
        # 부분 배열을 한칸으로 처리하는 연산
        if k >= 5: spin_arr_2(k, l, x, y)
    arr = new_arr # 배열 정보 갱신
  # 연산을 수행한 결과 출력
  for i in arr: print(' '.join(map(str,i)))

def main():
  global N, R, arr, commands
  N, R = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(2**N)]
  # k, ℓ
  commands = [list(map(int,input().split())) for _ in range(R)]
  solution() # 실행

if __name__ == "__main__":
  main()