# 2023/08/16 Implementation, String
# https://www.acmicpc.net/problem/28432
word_list = []
s = False
e = False
flag = False
for _ in range(int(input())):
  word = input()
  if word == '?': # 구해야 하는 문자열인 경우
    flag = True 
    if word_list: # 이전 단어가 있는 경우
      # ?의 첫문자, 이전 단어의 마지막 문자를 저장한다.
      s = word_list[-1][-1]
  else: # 평범한 끝말잇기 기록인 경우
    word_list.append(word)
    if flag and not e: # ?가 나오고, e가 지정되지 않은 경우
      # ?의 마지막 문자에 해당하는 문자를 저장한다.
      e = word_list[-1][0]

res = ""
for _ in range(int(input())):
  word = input()
  if not len(word_list): # 끝말잇기 기록이 없는 경우
    res = word
  if word not in word_list: # 이전에 사용되지 않은 단어인 경우 
    if word[0] == s and word[-1] == e:
      res = word
    if not s or not e: # 앞 문자를 구하지 못했거나, 뒤의 문자를 구하지 못한 경우
      if word[0] == s or word[-1] == e: # 둘 중 하나만 같이도 정답 처리
        res = word
print(res) # 정답 출력