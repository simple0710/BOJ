# 2023/08/23 BFS
# https://www.acmicpc.net/problem/9019
from collections import deque
import sys
input = sys.stdin.readline

def solution(A, B):
  q = deque([A])
  visited = [-1] * 10000
  visited[A] = ""
  while q:
    v = q.popleft()
    if v == B: # B를 만든 경우 해당 값(연산) 반환
      return visited[B]
    # DSLR 값 저장
    dict_ = {}
    dict_["D"] = 2 * v % 10000
    dict_["S"] = (v-1) % 10000
    dict_["L"] = v // 1000 + (v % 1000) * 10
    dict_["R"] = v // 10 + (v % 10) * 1000
    for d in ["D", "S", "L", "R"]:
      if visited[dict_[d]] == -1:
        visited[dict_[d]] = visited[v] + d
        q.append((dict_[d]))

def main():
  T = int(input())
  for _ in range(T):
    A, B = map(int,input().split())
    print(solution(A, B)) # 탐색 및 정답 출력

if __name__ == "__main__":
  main()