N, C = map(int,input().split())
T = int(input())
box = []
for _ in range(T):
  no, trans, cnt = map(int,input().split())
  box.append([no, trans, cnt])

box.sort(key=lambda x: x[1])

my_box = [C] * (N+1)
res = 0
for s, e, b in box:
  check = C
  for i in range(s, e):
    check = min(check, my_box[i])

  check = min(check, b)
  for i in range(s, e):
    my_box[i] -= check
    
  res += check

print(res)