# 2023/06/12 Implementation, Greedy, String
# https://www.acmicpc.net/problem/1213
from collections import defaultdict

word = input()
word_cnt = defaultdict(int)
for i in word: # 문자 개수 확인
  word_cnt[i] += 1
check = 0
check_word = ""
for i in word_cnt:
  if word_cnt[i] % 2 == 1: # 나누어서 남는게 있는 경우
    check += 1
    check_word = i
    if check > 1: # 2개 이상인 경우 팰린드롬 불가능
      print("I'm Sorry Hansoo")
      break
else: # 팰린드롬이 가능한 경우
  res = ""
  for i in sorted(word_cnt.keys()): # 앞부분
    res += i * (word_cnt[i] // 2)
  res_add = res[::-1] # 뒷부분
  if check == 1: # 나누어서 남는게 하나인 경우 해당 문자열 추가
    res += check_word
  # 정답 출력
  print(res + res_add)