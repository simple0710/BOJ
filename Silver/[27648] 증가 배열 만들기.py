# 2023/03/04 Ad-Hoc
# https://www.acmicpc.net/problem/27648
N, M, K = map(int,input().split())
res = [[0] * M for _ in range(N)]
res[0][0] = 1
moves = [(1, 0), (0, 1)]
flag = True
for i in range(N):
  for j in range(M):
    for k in range(2):
      nx = i + moves[k][0]
      ny = j + moves[k][1]
      # 해당 구역에 자신보다 큰 값을 넣는다.
      if nx < N and ny < M and res[i][j] >= res[nx][ny]:
        res[nx][ny] = res[i][j] + 1
        # 값이 K보다 크면 불가능
        if res[nx][ny] > K:
          flag = False
# 가능한 경우 'YES'와 배열 출력
if flag:
  print("YES")
  for i in res:
    print(*i)
# 불가능한 경우 'NO'출력
else:
  print("NO")