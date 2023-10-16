# 2023/08/17 MST, String
# https://www.acmicpc.net/problem/1414
import sys
input = sys.stdin.readline

def find(parent, x): # 부모 루트 찾기
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b): # 부모 루트 합치기
  a = find(parent, a)
  b = find(parent, b)
  parent[max(a, b)] = min(a, b)

def solution(N, data):
  lan = []
  res = 0
  for i in range(N):
    for j in range(N):
      if data[i][j] != '0':
        if ord(data[i][j]) >= 97: # 소문자인 경우
          d = ord(data[i][j]) - 96
        else: # 대문자인 경우
          d = ord(data[i][j]) - 38

        if i != j:
          lan.append((d, i, j))
        else: # 자기 자신의 랜선은 필요가 없다.
          res += d

  lan.sort() # 비용순으로 정렬

  parent = [i for i in range(N)]
  for c, x, y in lan:
    if find(parent, x) != find(parent, y): # 부모 루트가 다른 경우
      union(parent, x, y)
    else: # 필요 없는 랜선
      res += c

  for i in range(N):
    if find(parent, i) != 0: # 연결이 되지 않은 경우
      return -1
  return res

def main():
  N = int(input())
  data = [list(input().rstrip()) for _ in range(N)]
  print(solution(N, data)) # 탐색 및 정답 출력

if __name__ == "__main__":
  main()