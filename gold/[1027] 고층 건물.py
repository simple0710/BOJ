# 2023/11/05 Math, Gerometry, Bruteforcing
# https://www.acmicpc.net/problem/1027
import sys
input = sys.stdin.readline

# 기울기를 반환하는 함수
# (height2 - height1) / (width2 - width1)
def get_slope(data, now, next): return (data[now] - data[next]) / (now - next)

# 왼쪽 빌딩 탐색
def find_left(N, data, now):
  if now - 1 < 0: # 탐색할 건물이 없다면 0 반환
    return 0
  cnt = 1
  left = now - 1
  left_v = get_slope(data, now, left) # 가장 근처에 있는 빌딩 기울기 저장
  while left > 0:
    left -= 1
    new_left_v = get_slope(data, now, left) # 기울기 확인
    # 확인할 빌딩의 기울기가 확인한 빌딩의 기울기보다 작다면 보인다.
    if left_v > new_left_v:
      cnt += 1
      left_v = new_left_v
  return cnt # 보이는 빌딩 수 반환

# 오른쪽 빌딩 탐색
def find_right(N, data, now):
  if now + 1 >= N: # 탐색할 빌딩이 없으면 0 반환
    return 0
  cnt = 1
  right = now + 1
  right_v = get_slope(data, now, right) # 가장 근처에 있는 빌딩 기울기 저장
  while right < N-1:
    right += 1
    new_right_v = get_slope(data, now, right) # 기울기 확인
    # 확인할 빌딩의 기울기가 확인한 빌딩의 기울기보다 크다면 보인다.
    if right_v < new_right_v:
      cnt += 1
      right_v = new_right_v
  return cnt # 보이는 빌딩 수 반환

def solution(N, data):
  res = 0
  for i in range(N): # 모든 구역 확인
    res = max(res, find_left(N, data, i) + find_right(N, data, i))
  return res # 보이는 빌딩 수 반환

def main():
  N = int(input()) # 빌딩의 수
  data = list(map(int,input().split())) # 빌딩의 높이
  print(solution(N, data)) # 보이는 빌딩 수 출력

if __name__ == "__main__":
  main()