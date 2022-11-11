# 2022/11/08 브루트포스

def sol():
  res = 0
  # 모든 위치에서 인접한 부근과 스왑을 해본다.
  # search()를 수행한다.
  # 다시 원래 자리로 돌려둔다.
  for i in range(N):
    for j in range(N):
      if j + 1 < N:
        data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        temp = search(data, res)
        if temp > res:
          res = temp
        data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
      if i + 1 < N:
        data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
        temp = search(data, res)
        if temp > res:
          res = temp
        data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
        
  return res

# 먹을 수 있는 사탕의 최대 길이를 구한다.
# 행과 열에 대해서 각각 구하고 더 큰 cnt의 값이 나올 경우 값을 바꾼다.
def search(list, res):
  for i in range(N):
    cnt = 1
    for j in range(1, N):
      if list[i][j] == list[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      if cnt > res:
        res = cnt

    cnt = 1
    for j in range(1, N):
      if list[j][i] == list[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      if cnt > res:
        res = cnt

  return res

if __name__ == "__main__":
  # 정보 입력
  N = int(input())
  data = [list(map(str, input())) for _ in range(N)]

  res = sol()

  print(res)