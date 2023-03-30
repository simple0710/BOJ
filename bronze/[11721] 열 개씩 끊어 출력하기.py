# 2023/03/30 Implementation, String
# https://www.acmicpc.net/problem/11721
word = input()
# 10개씩 끊어서 정답 출력
for i in range(0, len(word), 10):
  print(word[i:i+10])