# 2023/10/28 Implementation, Simulation
# https://www.acmicpc.net/problem/1244
import sys
input = sys.stdin.readline

def solution(switch_cnt, situation, studens_cnt, get_switch):
  for gender, number in get_switch:
    if gender == 1: # 남자인 경우
      # 스위치 번호의 배수의 상태를 바꾼다.
      for i in range(number-1, switch_cnt, number):
        situation[i] = 1 - situation[i]
    elif gender == 2: # 여자인 경우
      # 좌우로 확인한 후, 상태가 같은 가장 큰 영역을 확인하고 상태를 변경한다.
      number -= 1
      situation[number] = 1 - situation[number]
      s = number - 1
      e = number + 1
      while s >= 0 and e < switch_cnt and situation[s] == situation[e]:
        situation[s] = 1 - situation[s]
        situation[e] = 1 - situation[e]
        s -= 1
        e += 1
  # 20개씩 끊어서 출력
  for i in [situation[i:i+20] for i in range(0, switch_cnt, 20)]:
    print(' '.join(map(str, i)))

def main():
  switch_cnt = int(input())
  situation = list(map(int,input().split()))
  students_cnt = int(input())
  # 성별, 스위치 번호
  get_switch = [list(map(int,input().split())) for _ in range(students_cnt)]
  solution(switch_cnt, situation, students_cnt, get_switch)

if __name__ == "__main__":
  main()