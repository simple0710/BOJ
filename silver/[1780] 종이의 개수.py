import sys
sys.setrecursionlimit(10**6)

def recur(x, y, n):
  global zero, one, m_one
  check_num = data[x][y]
  # 자신의 좌표부터 n까지의 거리
  for i in range(x, x + n):
    for j in range(y, y + n):
      # 다른 수가 보였을 경우
      if data[i][j] != check_num:
        # 9등분 하기
        for k in range(3):
          for l in range(3):
            # 내가 시작한 부분 + (0, 1, 2) * n // 3 
            # n = 9인 경우
            # 0 0 3, 0 3 3, 0 6 3
            # 3 0 3, 3 3 3, 3 6 3
            # 6 0 3, 6 3 3, 6 6 3
            recur(x+k*n//3, y+l*n//3, n//3)
        return
  if check_num == 0:
    zero += 1
  elif check_num == 1:
    one += 1
  elif check_num == -1:
    m_one += 1
  return
  
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

m_one, one, zero = 0, 0, 0
recur(0, 0, n)

print(m_one)
print(zero)
print(one)