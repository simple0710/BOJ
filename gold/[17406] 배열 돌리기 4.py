# 2023/09/17 Implementation, Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/17406
import sys
input = sys.stdin.readline

def arr_turn(r, c, s, arr):
  new_arr = [[[] for _ in range(M)] for _ in range(N)]
  rms = r-s
  rps = r+s # N
  cms = c-s
  cps = c+s # M
  # N => rps, M => cps
  for i in range(min(rps, cps)//2):
    # 주석에서 화살표와 괄호가 나오는 경우의 의미는 진행 방향(배열의 위치)로 한다.
    # rms, cms를 더한 경우는 해당 구역부터 시작된 값이기 때문이다.
    # rps, cps는 N, M과 비슷한 역할로 사용한다.
    # 첫자리 비우고 →(위), ←(아래)
    for j in range(i+1, cps-cms+1-i):
      new_arr[i+rms][j+cms] = arr[i+rms][j+cms-1]
      new_arr[rps-i][cps-j] = arr[rps-i][cps-j+1]
    # 첫자리도 채우고 ↑(왼쪽), ↓(오른쪽)
    for j in range(i, rps-rms-i):
      new_arr[j+rms][cms+i] = arr[j+rms+1][cms+i]
      new_arr[rps-j][cps-i] = arr[rps-j-1][cps-i]
  # 나머지 배열 채우기
  for i in range(N):
    for j in range(M):
      if not new_arr[i][j]: # 채우지 못한 배열이 있는 경우
        new_arr[i][j] = arr[i][j] # 원래 있던 배열값으로 채운다.
  return new_arr

def back(s_set, arr):
  global res
  if len(s_set) == len(command): # 모든 연산을 완료한 경우
    for i in arr:
      res = min(res, sum(i)) # 행의 합이 가장 작은 경우로 갱신
    return
  for idx, (r, c, s) in enumerate(command):
    if idx not in s_set: # 남은 연산이 있는 경우 연산 수행
      back(s_set | {idx}, arr_turn(r-1, c-1, s, arr))

def solution(arr):
  global res
  res = int(1e9)
  back(set(), arr) # 탐색 시작
  return res # 정답 반환

def main():
  global N, M, K, command
  N, M, K = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(N)]
  command = [list(map(int,input().split())) for _ in range(K)]
  print(solution(arr)) # 정답 출력

if __name__ == "__main__":
  main()