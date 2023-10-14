# 2023/10/15 Implementation, String
# https://www.acmicpc.net/problem/2607
from collections import defaultdict
import sys
input = sys.stdin.readline
# 한 문자 추가, 빼기, 하나의 문자를 다른 문자로 바꾸는 경우

# Solution 1
# 딕셔너리를 이용한 풀이
def solution1(words):
  word_cnt_dict = dict()
  # 각 단어의 알파벳 개수를 구한다.
  for word in words:
    cnt_dict_v = defaultdict(int)
    for i in word:
      cnt_dict_v[i] += 1
    word_cnt_dict[word] = cnt_dict_v

  res = 0
  for word in words[1:]:
    diff = 0
    gap = sys.maxsize
    # 모든 문자 확인 후 다른 점을 찾는다.
    for i in range(ord('A'), ord('Z')+1):
      check = abs(word_cnt_dict[words[0]][chr(i)] - word_cnt_dict[word][chr(i)])
      if check: # 1이상 차이가 나는 경우
        diff += 1 # 다른 경우 추가
        gap = min(gap, check) # 격차 갱신
    if diff == 0: # 다른 부분이 없는 경우
      res += 1
    elif gap == 1: # 한 문자만 다른 경우
      if diff == 1: # 다른 경우가 하나인 경우
        res += 1
      # 하나의 문자를 다른 문자로 교환하는 경우
      elif diff == 2 and len(words[0]) == len(word):
        res += 1
  return res # 비슷한 단어의 개수 반환

# Solution 2
# remove를 이용한 풀이
def solution2(words):
  res = 0
  for word in words[1:]:
    check = list(words[0])
    cnt = 0
    for w in word:
      if w in check: # 있으면 제거
        check.remove(w)
      else: # 없으면 cnt 증가
        cnt += 1
    # 없는 문자가 1개 이하이고, 남은 문자가 1개 이하인 경우
    if cnt < 2 and len(check) < 2:
      res += 1
  return res # 비슷한 단어의 개수 반환

def main():
  N = int(input())
  words = [input().rstrip() for _ in range(N)]
  # print(solution(words))

if __name__ == "__main__":
  main()