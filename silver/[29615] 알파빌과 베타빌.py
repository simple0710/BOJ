# 2023/09/03 Greedy
# https://www.acmicpc.net/problem/29615
import sys
input = sys.stdin.readline

def solution():
  res = 0
  for i in range(M):
    # 현재 위치가 친구가 아닌 경우 위치를 친구와 변경한다.
    if w_data[i] not in friends:
      res += 1
  print(res) # 정답 출력
  
if __name__ == "__main__":
  N, M = map(int,input().split())
  w_data = list(map(int,input().split()))
  friends = list(map(int,input().split()))
  solution()