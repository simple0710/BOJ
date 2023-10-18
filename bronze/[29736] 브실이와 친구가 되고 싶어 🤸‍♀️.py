# 2023/09/10 Math, Implementation
# https://www.acmicpc.net/problem/29736
import sys
input = sys.stdin.readline

def solution():
  # 친구의 수는 K-X, A중 큰 값 부터 K+X, B중 가장 작은 값까지의 사람끼리 친구를 할 수 있다.
  # 친구의 수 반환
  return len([i for i in range(max(K-X, A), min(K+X, B)+1)])

if __name__ == "__main__":
  A, B = map(int,input().split())
  K, X = map(int,input().split())
  res = solution() # 친구 수
  print(res if res else "IMPOSSIBLE") # 친구가 될 수 있는 사람이 있는 경우