# 2023/10/09 String
# https://www.acmicpc.net/problem/20437
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(W, K):
  word_list = defaultdict(list)
  res1 = 10001
  res2 = 0
  # 인덱스 저장
  for i in range(len(W)):
    word_list[W[i]].append(i)
  # 값 구하기
  for idx_list in word_list.values():
    # K개 이상인 알파벳으로 탐색한다.
    for j in range(K-1, len(idx_list)):
      res1 = min(res1, idx_list[j] - idx_list[j-(K-1)] + 1)
      res2 = max(res2, idx_list[j] - idx_list[j-(K-1)] + 1)
  if res1 == 10001 or res2 == 0: # 값이 없는 경우
    print(-1)
  else: # 값이 있는 경우
    print(res1, res2)

def main():
  T = int(input())
  for _ in range(T):
    W = input().rstrip()
    K = int(input())
    solution(W, K) # 탐색 시작

if __name__ == "__main__":
  main()