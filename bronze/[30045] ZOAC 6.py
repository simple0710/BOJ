# 2023/09/22 Implementation, String
# https://www.acmicpc.net/problem/30045
c = 0
for _ in range(int(input())):
  w = input() # 문장 입력
  # 01이 있거나, OI가 있는 경우
  if '01' in w or 'OI' in w:
    c += 1
print(c) # 이모티콘을 넣은 횟수 출력