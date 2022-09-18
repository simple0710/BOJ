result = []
arr = []
cnt = 1
check = 0
for i in range(int(input())):
  n = int(input())
  # cnt가 n보다 작거나 같으면 push 수행
  while cnt <= n:
    arr.append(cnt)
    result.append('+')
    cnt += 1
  # 마지막 부분이 n과 같다면 pop 수행
  if arr[-1] == n:
    arr.pop()
    result.append('-')
  else:
    print("NO")
    check = 1
    break
if check == 0:
  for i in result:
    print(i)
