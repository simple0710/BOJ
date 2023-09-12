# 2023/08/18 Math, Ad-Hoc
# https://www.acmicpc.net/problem/29196
import sys
input = sys.stdin.readline

def main():
  K = float(f'{float(input()):0.8f}')
  q = 10 ** 9
  # 두 수중 작은 값으로 계산한다.
  if 1 - K < K:
    if q % ((1 - K) * (10**8)) == 0:
      q /= (1 - K) * (10**8)
  else:
    if q % ((K) * (10**8)) == 0:
      q /= K * 10**8
  p = K * q
  check = K - (p / q)
  # 반올림
  if p - int(p) >= 0.5:
    p = int(p) + 1
  if q - int(q) >= 0.5:
    q = int(q) + 1
  # 정답 여부 확인
  if check <= 10**(-6) or K / check <= 10**(-6):
    print('YES')
    print(int(p), int(q))
  else:
    print("NO")

if __name__ == "__main__":
  main()