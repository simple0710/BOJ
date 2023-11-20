# 2023/08/26 DataStructures, Stack
# https://www.acmicpc.net/problem/1918
import sys
input = sys.stdin.readline

def solution(s):
  c = []
  res = ''
  for i in s:
    if i.isalpha(): # 알파벳인 경우
      res += i
    else:
      if i == '(': # 열린 괄호
        c.append(i)
      elif i == '*' or i == '/': # 곱셈 또는 나눗셈인 경우
        while c and (c[-1] == '*' or c[-1] == '/'): # 이전의 곱셈, 나눗셈을 res에 더한다.
          res += c.pop()
        c.append(i)
      elif i == '+' or i == '-': # 덧셈 또는 뺄셈인 경우
        while c and c[-1] != '(': # 열린 괄호가 아닌 경우 res에 추가한다.
          res += c.pop()
        c.append(i)
      elif i == ')': # 닫힌 괄호
        while c and c[-1] != '(': # 열린 괄호가 아닌 경우 res에 추가한다.
          res += c.pop()
        c.pop() # 열린 괄호 제거
  while c: # 나머지 값 res에 저장
    res += c.pop()
  return res # 정답 반환

if __name__ == "__main__":
  s = input().rstrip()
  print(solution(s))