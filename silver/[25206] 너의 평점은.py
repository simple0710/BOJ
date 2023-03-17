# 2023/03/16 Implementation, String
# https://www.acmicpc.net/problem/25206
p = 0 # (학점 * 과목평점)의 합
s = 0 # 학점의 총합
for _ in range(20):
  t = input().split()
  # 각 경우에 따른 분기
  if t[2] == 'P':
    continue
  s += float(t[1]) # 학점의 총합 더하기
  if t[2] == 'F':
    continue
  if t[2][0] == 'A':
    d = 4.0
  elif t[2][0] == 'B':
    d = 3.0
  elif t[2][0] ==  'C':
    d = 2.0
  else:
    d = 1.0
  if t[2][1] == '+':
    d += 0.5
  p += float(t[1]) * d # (학점 * 과목평점)의 합 더하기
# 정답 출력
print(round(p/s, 6))