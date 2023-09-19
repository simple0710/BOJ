# 2023/09/02 Implementation
# https://www.acmicpc.net/problem/16935
import sys
input = sys.stdin.readline

def turn(r, arr):
  global N, M
  new_arr = [[[] for _ in range(M)] for _ in range(N)]
  if r == 1: # 상하 반전
    for x in range(N//2):
      new_arr[x], new_arr[N-1-x] = arr[N-1-x], arr[x]
  elif r == 2: # 좌우 반전
    for x in range(N):
      new_arr[x] = arr[x][::-1]
  elif r == 3: # 오른쪽 90도 회전
    new_arr = list(zip(*arr[::-1]))
    N, M = M, N
    for i in range(N):
      new_arr[i] = list(new_arr[i])
  elif r == 4: # 왼쪽 90도 회전
    new_arr = list(zip(*arr))[::-1]
    N, M = M, N
    for i in range(N):
      new_arr[i] = list(new_arr[i])
  elif r == 5: # 4 그룹 시계방향 회전
    for x in range(N//2):
      new_arr[x][M//2:] = arr[x][:M//2]
      new_arr[x+N//2][M//2:] = arr[x][M//2:]
      new_arr[x+N//2][:M//2] = arr[x+N//2][M//2:]
      new_arr[x][:M//2] = arr[x+N//2][:M//2]
  elif r == 6: # 4 그룹 반시계방향 회전
    for x in range(N//2):
      new_arr[x+N//2][:M//2] = arr[x][:M//2]
      new_arr[x][:M//2] = arr[x][M//2:]
      new_arr[x][M//2:] = arr[x+N//2][M//2:]
      new_arr[x+N//2][M//2:] = arr[x+N//2][:M//2]

  return new_arr # 결과 반환

def solution(arr):
  for d in r_list: # 연산 수행
    arr = turn(d, arr)
  return arr # 배열 반환

if __name__ == "__main__":
  N, M, R = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(N)]
  r_list = list(map(int,input().split()))
  res = solution(arr)
  for i in res: # 정답 출력
    print(' '.join(map(str, i)))