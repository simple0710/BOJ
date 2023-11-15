# 2023/09/03 DataStructures, Greedy
# https://www.acmicpc.net/problem/25918
import sys
input = sys.stdin.readline

def solution():
  res = 0
  cnt = 0
  for i in string:
    # 괄호 확인
    if i == '(':
      cnt += 1
    elif i == ')':
      cnt -= 1
    # 가장 많이 쌓인 타이밍을 최대 일 수로 한다.
    res = max(res, abs(cnt))
  if cnt: # 괄호가 남은 경우 찢기 불가능
    res = -1
  print(res) # 정답 출력

if __name__ == "__main__":
  N = int(input())
  string = input().rstrip()
  solution() # 탐색 시작