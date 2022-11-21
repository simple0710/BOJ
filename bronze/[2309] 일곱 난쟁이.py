# 2022/11/08 백트래킹, 브루트포스
# 총 합에서 두명을 뺐을 경우 합이 100이 되면 정답출력을 하는 방법도 있다.
import sys
sys.setrecursionlimit(10**5)

def back():
  # 7명에 키의 합이 100인 경우 출력하고 종료
  if len(s) == 7 and sum(s) == 100:
    s.sort()
    for i in s:
      print(i)
    sys.exit()
  for i in data:
    if i not in s:
      s.append(i)
      back()
      s.pop()
# 정보 입력
data = []
for _ in range(9):
  data.append(int(input()))
data.sort()
s = []
back()


