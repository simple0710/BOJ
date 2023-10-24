# 2023/10/24 String, Greedy
# https://www.acmicpc.net/problem/20310
import sys
input = sys.stdin.readline

def solution(string):
  zero_cnt = string.count('0') // 2
  one_cnt = string.count('1') // 2
  res = ''
  for i in string:
    # 0을 먼저 절반만큼 추가한다.
    if i == '0' and zero_cnt:
      zero_cnt -= 1
      res += i
    elif i == '1': # 1은 나중에 추가한다.
      if one_cnt: # 절반의 횟수를 넘긴다.
        one_cnt -= 1
      else: # 절반 이후엔 정답에 추가한다.
        res += i
  return res # 문자열 반환

def main():
  string = input().rstrip()
  print(solution(string)) # 사전순으로 가장 빠른 문자열 출력

if __name__ == "__main__":
  main()