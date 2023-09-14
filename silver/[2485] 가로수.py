# 2023/09/14 Math, Euclidean
# https://www.acmicpc.net/problem/2485
import sys
input = sys.stdin.readline

def gcd(a, b): # 유클리드 호제법
  while b > 0:
    a, b = b, a % b
  return a # 최대공약수 반환

def solution(N, tree):
  # 가로수 사이의 간격 저장
  arr = [tree[i] - tree[i-1] for i in range(1, N)]

  # 최대공약수 구하기
  g = arr[0]
  for i in range(1, N-1):
    g = gcd(g, arr[i])

  # 가로수 간격을 구하는 방법 : 간격의 합 // 최대공약수 - 간격의 개수
  res = sum(arr) // g - (N - 1)
  return res # 정답 반환

def main():
  N = int(input())
  tree = [int(input()) for _ in range(N)]
  print(solution(N, tree)) # 정답 출력

if __name__ == "__main__":
  main()