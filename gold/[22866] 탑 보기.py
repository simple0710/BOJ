# 2023/11/08 DataStructures, Stack
# https://www.acmicpc.net/problem/22866
import sys
input = sys.stdin.readline
MAX = sys.maxsize

def solution(N, data):
  res = [[] for _ in range(N)]
  # 왼쪽 건물 확인
  left = []
  for i in range(N):
    # 더 큰 건물이 있을 때까지 반복한다.
    while left:
      if data[left[-1]] > data[i]:
        break
      left.pop()
    # 길이와 번호를 저장한다.
    res[i].append((len(left), left[-1] + 1 if left else MAX))
    left.append(i)
  
  # 오른쪽 건물 확인
  right = []
  for i in range(N):
    # 더 큰 건물이 있을 때까지 반복한다.
    while right:
      if data[right[-1]] > data[N-1-i]:
        break
      right.pop()
    # 길이와 번호를 저장한다.
    res[N-1-i].append((len(right), right[-1] + 1 if right else MAX))
    right.append(N-1-i)

  # 정답 출력
  for i in range(N):
    left, right = res[i]
    if max(left[0], right[0]) == 0: # 볼 수 있는 건물이 없는 경우
      print(0)
    else: # 볼 수 있는 건물이 있는 겅우
      ni = i + 1 # 번호
      # 가장 가까이 있는 건물의 번호를 확인한다.
      near = left[1] if abs(ni - left[1]) <= abs(ni - right[1]) else right[1]
      # 볼 수 있는 건물의 수, 가까이 있는 건물의 번호 출력
      print(left[0] + right[0], near)

def main():
  # 건물의 수
  N = int(input())
  # 건물의 높이
  data = list(map(int,input().split()))
  solution(N, data)  

if __name__ == "__main__":
  main()