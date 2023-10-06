# 2023/10/06 Implementation, Bruteforcing
# https://www.acmicpc.net/problem/2784
from itertools import permutations
import sys
input = sys.stdin.readline

def check(board):
  # 가로 세로 단어를 확인
  check_board = [words[i] for i in board]
  for i in range(3):
    w = ''
    for j in board:
      w += words[j][i]
    check_board.append(w)
  # 처음 주어진 단어들과 같은 경우 True
  return True if words == sorted(check_board) else False

def back(): # 퍼즐에 둘 수 있는 모든 경우의 수 구하기
  if len(board) == 3: # 3단어를 나열한 경우
    if check(board): # 단어 확인 후 모든 단어가 포함된 경우
      res_list.add(tuple([words[i] for i in board]))
    return
  for i in range(6): # 모든 경우 확인
    if i not in board:
      board.append(i)
      back()
      board.pop()

def solution1(): 
  global board, res_list
  res_list = set()
  board = list()
  back() # 조합 탐색
  if res_list: # 정답이 있는 경우
    for i in sorted(list(res_list))[0]:
      print(i)
  else: # 정답이 없는 경우
    print(0)

def solution2():
  idx = [i for i in range(6)]
  perm = list(permutations(idx, 3))
  res = []
  for p in perm: # 모든 조합 확인
    check = []
    for i in p: # 가로 확인
      check.append(words[i])
    for i in range(3): # 세로 확인
      w = ''
      for j in p:
        w += words[j][i]
      check.append(w)
    if sorted(check) == words: # 주어진 문자열을 전부 놓은 경우
      res.append(p)
  if res: # 정답이 있는 경우 사전순으로 가장 앞서는 정답 출력
    for i in sorted(res)[0]:
      print(words[i])
  else: # 정답이 없는 경우
    print(0)

def main():
  global words
  words = sorted([input().rstrip() for _ in range(6)])
  # solution()

if __name__ == "__main__":
  main()