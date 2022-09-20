word = input()
data = list()
for i in range(len(word)):
  data.append(word[i:])
data.sort()
for i in data:
  print(i)