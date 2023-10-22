# 2023/09/10 Implementation, DataStructures, Hash-Set
# https://www.acmicpc.net/problem/29721
import sys
input = sys.stdin.readline

if __name__ == "__main__":
  dx = [0, -2, 2, 0, 0]
  dy = [0, 0, 0, -2, 2]
  # 체스판 크기, 다바바의 개수
  N, K = map(int,input().split())
  check_list = set()
  for _ in range(K):
    # 다바바 위치
    x, y = map(int,input().split())
    for i in range(5): # 위치 확인
      nx = x - 1 + dx[i]
      ny = y - 1 + dy[i]
      # 범위 안, 이동할 수 있는 위치인 경우
      if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in check_list:
        check_list.add((nx, ny)) # 집합에 추가
  print(len(check_list) - K) # 정답 출력