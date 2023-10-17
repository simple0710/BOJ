# 2023/10/17 DataStructures, Bruteforcing
# https://www.acmicpc.net/problem/2304
import sys
input = sys.stdin.readline

# 배열을 오름차 순으로 확인한다.
# 배열 범위, 배열 값
def check_asc_arr(length, bar):
  cnt = 0
  max_height_idx = 0
  for i in range(1, length):
    # 현재 가장 큰 기둥보다 큰 기둥이 있다면 넓이를 더한다.
    if bar[max_height_idx][1] <= bar[i][1]:
      cnt += bar[max_height_idx][1] * abs(bar[max_height_idx][0] - bar[i][0])
      max_height_idx = i
  return (cnt, max_height_idx) # 넓이와 가장 큰 기둥의 인덱스를 반환

def solution(N, bar):
  bar.sort()
  # 왼쪽부터 오른쪽 탐색
  # 넓이 값과 가장 큰 기둥이 있는 곳의 인덱스를 받아온다.
  l_to_r, mh_idx = check_asc_arr(N, bar)
  # 오른쪽부터 왼쪽 방향 탐색(가장 큰 막대가 있는 곳의 전까지)
  # 넓이 값만 받아온다.
  r_to_l = check_asc_arr(N-mh_idx, bar[::-1])[0]
  # 위에서 구한 
  # 두 넓이의 값과 
  # 더해지지 못한 가장 큰 기둥의 넓이를 더한 값을 반환한다.
  return l_to_r + r_to_l + bar[mh_idx][1]

def main():
  N = int(input()) # 기둥의 개수
  bar = []
  for _ in range(N):
    # 왼쪽 면의 위치, 높이
    a, b = map(int,input().split())
    bar.append((a, b))
  print(solution(N, bar)) # 가장 작은 창고 다각형의 면적 출력

if __name__ == "__main__":
  main()