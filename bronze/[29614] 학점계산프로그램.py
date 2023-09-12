# 2023/09/03 Math, Implementation, String
# https://www.acmicpc.net/problem/29614
import sys
input = sys.stdin.readline

def solution():
  score = {
    'A' : 4,
    'B' : 3,
    'C' : 2,
    'D' : 1,
    'F' : 0,
    }
  total = 0
  total_cnt = 0
  cnt = 0
  while cnt < len(string):
    now = score[string[cnt]]
    if cnt + 1 < len(string):
      # +가 붙은 경우 0.5를 더하고, cnt이동 값을 1을 더 증가시킨다.
      if string[cnt+1] == '+':
        now += 0.5
        cnt += 1
    total += now
    total_cnt += 1
    cnt += 1
  print(f'{total / total_cnt:.5f}') # 정답 출력

if __name__ == "__main__":
  string = input().rstrip()
  solution()