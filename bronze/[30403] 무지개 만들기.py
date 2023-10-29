# 2023/10/28 Implementation, String
# https://www.acmicpc.net/problem/30403
import sys
input = sys.stdin.readline

def main():
  N = int(input())
  string = input().rstrip()
  res = 'NO!'
  # 소문자로 무지개 문자열을 만들 수 있는 경우
  for i in 'roygbiv':
    if i not in string:
      break
  else:
    res = 'yes'

  # 대문자로 무지개 문자열을 만들 수 있는 경우
  for i in 'ROYGBIV':
    if i not in string:
      break
  else:
    # 소문자, 대문자로 무지개 문자열을 만들 수 있는 경우
    if res == 'yes':
      res = 'YeS'
    elif res == 'NO!':
      res = 'YES'
  # 문자열로 무지개를 만들 수 있는지 출력
  print(res)

if __name__ == "__main__":
  main()