A, P = map(int,input().split())
arr = [A]
while True:
  sum = 0
  for i in str(arr[-1]):
    sum += int(i) ** P
  if sum in arr:
    break
  arr.append(sum)
  

print(arr.index(sum))