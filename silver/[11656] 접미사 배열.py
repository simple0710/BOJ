word = input()
data = list()
for i in range(len(word)):
  # 슬라이스를 하나씩 올림
  data.append(word[i:])
data.sort()
for i in data:
  print(i)