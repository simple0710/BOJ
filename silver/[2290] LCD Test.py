# 2023/12/20 implementation, String
# https://www.acmicpc.net/problem/2290
def draw_number(idx, number):
  # 상단, 중단, 하단 기준
  idx_check = {
    0: [['1', '4']],
    (2*s+3)//2: [['0', '1', '7'], ['1', '2', '3', '7'], ['5', '6']],
    2*s+3-1: [['1', '4', '7'], ['1', '3', '4', '5', '7', '9'], ['2']]
  }
  string = ''
  for key in idx_check:
    # 같은 값이라면 가로 문자 '-'를 사용해야 한다.
    # 1. 공백 + '-' * s + 공백
    # 2. 공백 + ' ' * s + 공백
    if idx == key:
      string += ' '
      if number not in idx_check[key][0]: string += '-'*s
      else: string += ' '*s
      string += ' '
      break
    # 중간에 위치하는 문자를 그려야 하는 경우 세로 문자 '|'를 사용해야 한다.
    # 1. '|' + ' ' * s + '|'
    # 2. '|' + ' ' * s + ' '
    # 3. ' ' + ' ' * s + '|'
    elif idx < key:
      if number not in idx_check[key][1]: string += '|'
      else: string += ' '
      string += ' '*s
      if number not in idx_check[key][2]: string += '|'
      else: string += ' '
      break
  print(string, end=' ') # 현재 숫자의 일부 그리기

def solution():
  for idx in range(2*s+3):
    # 현재 숫자의 일부를 그린다.
    for j in str(n): draw_number(idx, j)
    print()

def main():
  global s, n
  s, n = map(int,input().split())
  solution()

if __name__ == "__main__":
  main()