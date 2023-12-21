# 2023/12/21 Implementation, String
# https://www.acmicpc.net/problem/9093
for _ in range(int(input())):
  # 각 단어의 위치를 뒤집어서 출력한다.
  for i in input().split(): print(i[::-1],end=' ')
  print() # 줄바꿈