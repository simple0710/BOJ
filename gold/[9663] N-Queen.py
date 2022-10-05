def back(x):
  global cnt
  if x == n:
    cnt += 1
    return
  for i in range(n):
    row[x] = i # 퀸을 여기 두겠다는 의미
    if is_promising(x):
      back(x+1)  

def is_promising(x):
  for i in range(x):
    # 열이 같거나 대각선이 같으면 False
    # 대각선의 경우 행 - 행 == 열 - 열
    if row[x] == row[i] or abs(row[x]-row[i]) == abs(x - i):
      return False
  return True

n = int(input())
cnt = 0
# row = [1, 3, 0, 2] 인 경우 첫 줄에 1번 인덱스, 두번째 줄에 3번 인덱스를 의미
row = [0] * n 
back(0)
print(cnt)