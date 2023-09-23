# 2023/09/23 Implementation, Simulation
# https://www.acmicpc.net/problem/23291
import sys
input = sys.stdin.readline

# 물고기 수가 가장 적은 어항에 물고기 한마리 추가
def fishbowl_fill():
  global fishbowl
  v = min(fishbowl)
  for i in range(len(fishbowl)):
    if fishbowl[i] == v:
      fishbowl[i] += 1

# 어항 공중부양1
def fishbowl_levitation1():
  global fishbowl
  new_fishbowl = [[fishbowl[0]]]
  fishbowl = fishbowl[1:]
  # 놓을 수 있는 곳이 있는 경우 True
  while len(new_fishbowl) <= len(fishbowl):
    length = len(new_fishbowl)
    # 현재 어항 회전
    new_fishbowl = list(zip(*new_fishbowl[::-1]))
    # 어항 밑부분 추가
    new_fishbowl.append(fishbowl[:length])
    # 놓을 수 있는 어항 갱신
    fishbowl = fishbowl[length:]
  # 데이터 타입 변환
  for i in range(len(new_fishbowl)):
    new_fishbowl[i] = list(new_fishbowl[i])
  new_fishbowl[-1].extend(fishbowl) # 남은 어항 마지막에 추가
  fishbowl = new_fishbowl

# 물고기의 수 조절
# 차이를 5로 나눈 몫을 큰 어항엔 몫만큼 감소, 작은 어항엔 몫만큼 증가
# 동시 시행
def fishbowl_check():
  global fishbowl
  dx = [1, 0]
  dy = [0, 1]
  cnt_arr = []
  for i in range(len(fishbowl)): # 어항 모양 배열 생성
    cnt_arr.append([0] * len(fishbowl[i]))
  for x in range(len(fishbowl)):
    for y in range(len(fishbowl[x])):
      for i in range(2): # 오른쪽, 아래만 확인
        nx = x + dx[i] 
        ny = y + dy[i]
        # 범위를 벗어나지 않는 경우
        if nx < len(fishbowl) and ny < len(fishbowl[nx]):
          v = abs(fishbowl[x][y] - fishbowl[nx][ny]) // 5
          # x, y의 물고기 수가 더 많은 경우
          if fishbowl[x][y] > fishbowl[nx][ny]:
            v *= -1
          cnt_arr[x][y] += v
          cnt_arr[nx][ny] -= v
  # 물고기의 수 조절
  for x in range(len(fishbowl)):
    for y in range(len(fishbowl[x])):
      fishbowl[x][y] += cnt_arr[x][y]

# 어항 일렬로 나열
# 순서는 가장 왼쪽부터 시작(그리고 아래부터 위에 있는 어항 순)
def fishbowl_arrange():
  global fishbowl
  new_fishbowl = []
  # 시계 방향 회전을 하면 가장 위부터 추가하면 된다
  for i in zip(*fishbowl[::-1]):
    new_fishbowl.extend(list(i))
  fishbowl = new_fishbowl + fishbowl[-1][len(fishbowl[0]):]

# 어항 공중 부양 2
def fishbowl_levitation2():
  global fishbowl
  # 어항을 N//2만큼 나누고 남은 왼쪽을 180도 회전 후 오른쪽에 쌓는 것을 두 번한다.
  fishbowl = [list(fishbowl[:len(fishbowl)//2])[::-1], list(fishbowl[len(fishbowl)//2:])]
  up = []
  down = []
  for i in range(len(fishbowl)):
    up_arr = []
    down_arr = []
    for j in range(len(fishbowl[i])):
      if j < len(fishbowl[i]) // 2: # 왼쪽
        up_arr.append(fishbowl[i][j])
      else: # 오른쪽
        down_arr.append(fishbowl[i][j])
    up.append(up_arr[::-1])
    down.append(down_arr)
  up = up[::-1]
  fishbowl = [*up, *down]

def solution():
  global fishbowl
  '''
  가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가
  K이하인 경우 종료된다.
  '''
  res = 0
  while max(fishbowl) - min(fishbowl) > K:
    res += 1
    # 가장 작은 어항에 물고기 채우기
    fishbowl_fill()

    # 공중 부양1
    fishbowl_levitation1()
    # 인접한 어항 차이 확인
    fishbowl_check()
    # 어항 일렬로 나열
    fishbowl_arrange()

    # 공중 부양2
    fishbowl_levitation2()
    # 인접한 어항 차이 확인
    fishbowl_check()
    # 어항 일렬로 나열
    fishbowl_arrange()
  return res # 어항 정리 수 출력

def main():
  global N, K, fishbowl
  N, K = map(int,input().split())
  fishbowl = list(map(int,input().split()))
  print(solution()) # 코드 실행 및 정답 출력

if __name__ == "__main__":
  main()