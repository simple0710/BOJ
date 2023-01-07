# 2023/01/06 backtracking
# https://www.acmicpc.net/problem/2661
import sys
input = sys.stdin.readline

def back(s):
  # 맨 뒤에서 시작(새로운 값부터 확인하기 위함)
  for i in range(1, (len(s)//2) + 1):
    if s[-i:] == s[-2*i:-i]:
      return -1

  # 길이에 도달한 경우 정답 출력
  if len(s) == N:
    print(''.join(map(str, s)))
    sys.exit()

  # 1, 2, 3 중에 수를 하나 선택
  for i in range(1, 4):
    s.append(i)
    back(s)
    s.pop()

N = int(input())
s = [1]
back(s)