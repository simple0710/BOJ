# 2023/09/01 Implementation
# https://www.acmicpc.net/problem/16927
import sys
input = sys.stdin.readline

def solution():
  for x in range(min(N//2, M//2)):
    # 가장자리 배열 값 정렬
    data = [arr[x][i] for i in range(x, M-x)]
    data.extend([arr[i][M-1-x] for i in range(x+1, N-1-x)])
    data.extend([arr[N-1-x][i] for i in range(x, M-x)][::-1])
    data.extend([arr[i][x] for i in range(x+1, N-1-x)][::-1])

    # R만큼 회전
    nr = R % len(data)
    new_data = data[nr:] + data[:nr]

    # 회전한 배열 복구
    cnt = 0
    for i in range(x, M-x):
      arr[x][i] = new_data[cnt]
      cnt += 1
    for i in range(x+1, N-1-x):
      arr[i][M-1-x] = new_data[cnt]
      cnt += 1
    for i in range(M-x-1, x-1, -1):
      arr[N-1-x][i] = new_data[cnt]
      cnt += 1
    for i in range(N-1-1-x, x, -1):
      arr[i][x] = new_data[cnt]
      cnt += 1

if __name__ == "__main__":
  N, M, R = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(N)]
  solution()
  for i in arr: # 정답 출력
    print(' '.join(map(str, i)))