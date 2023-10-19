# 2023/09/10 Math
# https://www.acmicpc.net/problem/29720
import sys
input = sys.stdin.readline

def solution(a, b, c):
  now = b * c # M 문제를 K일 풀었을 경우의 총 문제 수
  min_ = a - now # N 문제를 해결하기까지 남은 최소 일 수,
  max_ = min_ + b - 1 # 최대로 푼 문제 수
  print(min_ if min_ > 0 else 0, max_) # 푼 문제 수의 최솟값과 최댓값 출력

if __name__ == "__main__":
  N, M, K = map(int,input().split())
  solution(N, M, K)