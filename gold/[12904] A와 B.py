s = list(input())
t = list(input())

# 발상의 전환, 작은 문자열에서 계산보다
# 큰 문자열에서 계산 해보는 것이 해결책
can = 0
while t:
  if t[-1] == "A":
    t.pop()
  elif t[-1] == "B":
    t.pop()
    t.reverse()
  if s == t:
    can = 1
    break

print(can)