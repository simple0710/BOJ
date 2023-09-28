# 2023/09/28 Implementation, Bruteforcing
# https://www.acmicpc.net/problem/2116
import sys
input = sys.stdin.readline

def value_get(top, bottom): # 옆면의 최댓값 큰 값 구하기
  return max([v for v in range(1, 7) if top != v and bottom != v])

def solution(N, dice):
  # A - F, B - D, C - E
  tb_dict = { 0 : 5, 1 : 3, 2 : 4, 4 : 2, 3 : 1, 5 : 0}
  res = 0
  for i in range(6): # 시작은 자유롭게 놓을 수 있다.
    top = dice[0][i]
    cnt = value_get(top, dice[0][tb_dict[i]])
    for j in range(1, N):
      bottom = top
      # 윗면은 밑면의 맞은편에 위치함
      top = dice[j][tb_dict[dice[j].index(bottom)]]
      cnt += value_get(top, bottom) # 옆면의 최댓값 더하기
    res = max(res, cnt) # 값 갱신
  return res # 정답 반환

def main():
  N = int(input())
  dice = []
  for _ in range(N):
    dice.append(list(map(int,input().split())))
  print(solution(N, dice)) # 코드 실행 및 정답 출력

if __name__ == "__main__":
  main()