# 2023/08/12 Implementation, Simulation
# https://www.acmicpc.net/problem/28456
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
Q = int(input())
for _ in range(Q):
  act = list(map(int,input().split()))
  if act[0] == 1: # 1번 행동
    # act[1]번째 행 선택 후, 마지막 행을 제거하고 첫 번째 원소 앞에 추가
    arr[act[1] - 1] = [arr[act[1] - 1][-1]] + arr[act[1] - 1][:N-1]
  else: # 2번 행동
    new_arr = [[0] * N for _ in range(N)]
    # 모든 i번째 행 j번째 열의 원소 -> j번째 행 N - i + 1번째 열의 원소
    for i in range(N):
      for j in range(N):
        new_arr[j][N - i - 1] = arr[i][j]
    arr = new_arr
for i in arr: # 정답 출력
  print(*i)