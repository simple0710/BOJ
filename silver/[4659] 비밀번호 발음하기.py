# 2023/01/25 문자열
# https://www.acmicpc.net/problem/4659
import sys
input = sys.stdin.readline
mo = ['a', 'e', 'i', 'o', 'u'] # 모음 배열(딕셔너리로도 가능하다.)

while True:
  words = input().rstrip()
  if words == 'end': # end인 경우 종료
    break
  zaCnt = 0
  moCnt = 0
  moFlag = False
  threeFlag = False
  sameFlag = False
  for i in range(len(words)):
    if i < len(words)-1: # 같은 문자 비교
      if words[i] == words[i+1] and (words[i] != 'e' and words[i] != 'o'):
        sameFlag = True
    if words[i] in mo: # 모음 개수 체크
      zaCnt = 0
      moCnt += 1
      if moCnt >= 3: # 3개 이상 연속된 경우
        threeFlag = True
        break
      moFlag = True
    else: # 자음 개수 체크
      moCnt = 0
      zaCnt += 1
      if zaCnt >= 3: # 3개 이상 연속된 경우
        threeFlag = True
        break
  # 정답 출력
  if moFlag and not threeFlag and not sameFlag: # 사용 가능한 패스워드인 경우
    print(f'<{words}> is acceptable.')
  else: # 사용 불가능한 패스워드인 경우
    print(f'<{words}> is not acceptable.')