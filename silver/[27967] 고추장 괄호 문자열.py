# 2023/04/24 Backtracking
# https://www.acmicpc.net/problem/27967
import sys
input = sys.stdin.readline

def back(s, w):
  if len(w) == N: # 끝까지 탐색한 경우
    check = 0
    for i in w:
      if i == '(':
        check += 1
      else:
        check -= 1
        if check < 0: # 닫는 기호가 더 많은 경우
          break
    else:
      if check == 0: # 두 기호의 수가 같으면 정답 출력 후 종료
        print(w)
        sys.exit(0)
    return

  for i in range(s, N):
    if data[i] == 'G':
      back(i+1, w+'(') # 여는 기호
      back(i+1, w+')') # 닫는 기호
    else:
      back(i+1, w+data[i])

N = int(input())
data = input()
# 탐색 시작
back(0, '')