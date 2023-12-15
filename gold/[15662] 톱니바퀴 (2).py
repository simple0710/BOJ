# 2023/12/15 Implementation, Simulation
# https://www.acmicpc.net/problem/15662
# 시계 방향 회전
def default_spin(now):
  gear[now] = gear[now][-1] + gear[now][:-1]

# 반 시계 방향 회전
def not_default_spin(now):
  gear[now] = gear[now][1:] + gear[now][0]

def solution():
  for num, turn in spin:
    num -= 1
    # 현재 톱니바퀴 상황 확인
    gear_check = [False] * (T-1)
    for i in range(T-1):
      if gear[i][2] == gear[i+1][6]: gear_check[i] = True
    # 시계 방향 회전인 경우
    if turn == 1:
      default_spin(num)
      # 현재 위치를 0이라 한다.
      # 다음 회전의 위치가 짝수면 시계 방향으로 회전한다.
      # 다음 회전의 위치가 홀수면 반시계 방향으로 회전한다.
      for i in range(num, 0, -1):
        if gear_check[i-1]: break
        if (num-i-1) % 2 == 0: default_spin(i-1)
        elif (num-i-1) % 2 == 1: not_default_spin(i-1)
      for i in range(num, T-1):
        if gear_check[i]: break
        if (i-num+1) % 2 == 0: default_spin(i+1)
        elif (i-num+1) % 2 == 1: not_default_spin(i+1)
    elif turn == -1:
      not_default_spin(num)
      # 현재 위치를 0이라 한다.
      # 다음 회전의 위치가 짝수면 반시계 방향으로 회전한다.
      # 다음 회전의 위치가 홀수면 시계 방향으로 회전한다.
      for i in range(num, 0, -1):
        if gear_check[i-1]: break
        if (num-i-1) % 2 == 0: not_default_spin(i-1)
        elif (num-i-1) % 2 == 1: default_spin(i-1)
      for i in range(num, T-1):
        if gear_check[i]: break
        if (i-num+1) % 2 == 0: not_default_spin(i+1)
        elif (i-num+1) % 2 == 1: default_spin(i+1)
  # 12시 방향이 S극인 톱니바퀴의 개수 확인
  res = 0
  for now in gear:
    if now[0] == '1': res += 1
  return res # 12시 방향이 S극인 톱니바퀴의 개수 반환

def main():
  global T, gear, K, spin
  T = int(input())
  gear = [input() for _ in range(T)]
  K = int(input())
  spin = [list(map(int,input().split())) for _ in range(K)]
  print(solution()) # 12시 방향이 S극인 톱니바퀴의 개수 출력

if __name__ == "__main__":
  main()