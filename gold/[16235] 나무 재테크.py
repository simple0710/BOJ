# 2023/06/14 Implementation, DataStructures, Simulation
# https://www.acmicpc.net/problem/16235
# 맨 처음 땅의 양분은 5
# 같은 칸에 여러 개의 나무가 심어질 수 있음. 

# 봄
# 나이가 작은 나무부터 양분 먹음
# 나이만큼 양분을 먹고 나이 1 증가. 양분이 부족하면 바로 죽음
def spring():
  for i in range(N):
    for j in range(N):
      check = []
      for t in tree[i][j]:
        if board[i][j] >= t: # 양분을 먹을 수 있는 경우
          board[i][j] -= t
          check.append(t + 1)
        else: # 양분을 먹을 수 없는 경우
          dead[i][j].append(t)
      tree[i][j] = check # tree[i][j]의 정보 변경

# 여름
# 봄에 죽은 나무가 양분으로 변함
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가. 소수점은 버림
def summer(): # 죽은 나무를 양분으로 변경
  for i in range(N):
    for j in range(N):
      for k in dead[i][j]:
        board[i][j] += k // 2

# 가을
# 나이가 5배수인 경우 인접한 8칸에 나이가 1인 나무 생성
# 범위를 벗어나면 나무 생성 x
def autumn():
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, 1, -1, -1, 0, 1]
  for i in range(N):
    for j in range(N):
      for t in tree[i][j]:
        if t % 5 == 0: # 5의 배수인 경우 인접한 8칸에 나이 1 나무 생성
          for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N: # 범위를 벗어나지 않는 경우
              tree[nx][ny].insert(0, 1) # 맨 앞에 추가

# 겨울
# 양분 추가, 각 칸에 추가되는 양분의 양은 A[r][c]로 주어진다.
def winter():
  for i in range(N):
    for j in range(N):
      board[i][j] += energy[i][j]

N, M, K = map(int,input().split()) # 땅의 크기, 나무의 수, K년
energy = [list(map(int,input().split())) for _ in range(N)] # S2D2 에너지

# 나무 정보 입력
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  a, b, z = map(int,input().split())
  a -= 1
  b -= 1
  tree[a][b].append(z)
  tree[a][b].sort() # 나이가 낮은 순으로 정렬한다.

# K년 반복
board = [[5] * N for _ in range(N)] # 맨 처음 땅의 양분
for _ in range(K):
  dead = [[[] for _ in range(N)] for _ in range(N)]
  spring() # 봄
  summer() # 여름
  autumn() # 가을
  winter() # 겨울

# 나무의 총 개수 구하기
res = 0
for i in range(N):
  for j in range(N):
    res += len(tree[i][j])

# 정답 출력
print(res)