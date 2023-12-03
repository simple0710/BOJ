# 2023/12/03 Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/16987
import sys
input = sys.stdin.readline

def back(now):
  global res
  # 맨 오른쪽 계란 까지 모두 시험했을 때,
  # 지금까지 깬 계란의 개수를 구한다.
  if now == N:
    total = 0
    for i in eggs:
      if i[0] <= 0: total += 1
    res = max(res, total)
    return
  # 현재 계란의 내구도가 0이라면 다음 계란을 든다.
  if eggs[now][0] <= 0:
    back(now + 1)
    return
  flag = False
  for i in range(N):
    # 깰 수 있는 계란이고, 같은 위치의 계란이 아니라면 쳐본다.
    if eggs[i][0] > 0 and i != now:
      flag = True
      # 내구도 - 무게 계산
      eggs[i][0] -= eggs[now][1]
      eggs[now][0] -= eggs[i][1]
      # 다음 계란 확인
      back(now + 1)
      eggs[i][0] += eggs[now][1]
      eggs[now][0] += eggs[i][1]
  # 깰 수 있는 계란이 없다면 깬 계란이 개수를 확인한다.
  if not flag: back(N)

def solution():
  global res
  res = 0
  back(0) # 탐색 시작
  return res # 깰 수 있는 계란의 최대 개수 반환

def main():
  global N, eggs
  N = int(input())
  # 계란 정보(내구도, 무게)
  eggs = [list(map(int,input().split())) for _ in range(N)]
  print(solution()) # 깰 수 있는 계란의 최대 개수 출력 

if __name__ == "__main__":
  main()