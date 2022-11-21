# 2022/11/17 구현
# 해당 문구가 나오면 그에 맞는 명령을 수행하면 해결할 수 있다.
import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
  temp = sys.stdin.readline().strip().split()
  if len(temp) == 1:
    if temp[0] == "all":
      S = set([i for i in range(1, 21)])
    else:
      S = set()
  else:
    func, x = temp[0], temp[1]
    x = int(x)

    if func == "add":
      S.add(x)
    elif func == "remove":
      S.discard(x)
    elif func == "check":
      print(1 if x in S else 0)
    elif func == "toggle":
      if x in S:
        S.discard(x)
      else:
        S.add(x)