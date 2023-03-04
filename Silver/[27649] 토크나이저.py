# 2023/03/04 구현
# https://www.acmicpc.net/problem/27649
import sys
input = sys.stdin.readline

word = ' '.join(input().rstrip().split())
res = []
s = 0
flag = False
for i in range(len(word)):
  if flag: # '&&' or '||'의 경우 두번째 경우는 넘긴다.
    flag = False
    continue
  # 해당 문자가 구분자인 경우ㄴ
  if word[i] in ['<', '>', '&', '|', '(', ')']:
    # 이전 문자열 저장
    res.append(word[s:i]) 
    # '&&' 또는 '||'가 연속으로 두개인 경우 2개의 값을 저장
    if i < len(word) - 1 and (word[i] == '|' and word[i+1] == '|') or (word[i] == '&' and word[i+1] == '&'):
      flag = True
      res.append(word[i:i+2])
      s = i + 2
    # 구분자가 아닌 경우
    else:
      res.append(word[i])
      s = i + 1
# 마지막에 남은 단어 더하기      
if s < len(word):
  res.append(word[s:])

# 정답 분류하기
res = ' '.join(map(str, res)).split()
res = ' '.join(res)

# 정답 출력
print(res)