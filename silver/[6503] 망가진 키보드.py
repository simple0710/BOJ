# 2023/04/28 TwoPointer
# https://www.acmicpc.net/problem/6503
from collections import defaultdict

def two_pointer():
  s = 0
  e = 0
  res = 0
  word_dict = defaultdict(int)
  while e < len(word):
    # 공간이 있거나 기존에 word[e]를 사용했던 경우
    if len(word_dict.keys()) + 1 <= M or word_dict[word[e]] > 0:
      word_dict[word[e]] += 1
      res = max(res, (e - s + 1))
      e += 1
    else: # 그렇지 않은 경우
      word_dict[word[s]] -= 1
      if word_dict[word[s]] <= 0: # word[s]의 값이 0이하인 경우 삭제
        word_dict.pop(word[s])
      if word_dict[word[e]] == 0: # 맨 위의 if문 실행시 word[e]가 생성됨
        word_dict.pop(word[e])
      s += 1
  # 정답 출력
  print(res)

while True:   
  M = int(input())
  if M == 0:
    break
  word = input()
  # 탐색 시작
  two_pointer()
