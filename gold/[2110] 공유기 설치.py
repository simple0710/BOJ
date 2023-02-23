# 2023/02/23 이분 탐색
# https://www.acmicpc.net/problem/2110
def search():
  start = 0
  end = data[-1] - data[0]
  res = 0
  while start <= end:
    mid = (start + end) // 2
    s = data[0]
    cnt = 1
    # 1부터 맨 끝까지 탐색 해본다. (왼쪽부터 설치해 본다.)
    for i in range(1, len(data)):
      # 현재 설치된 곳과 중간값의 합이 더 현재 좌표보다 더 큰 경우
      if data[i] >= s + mid:
        # 현재 설치된 곳의 값을 변경하고 cnt += 1을 한다.
        cnt += 1
        s = data[i]
    if cnt >= C: # 더 많은 공유기를 설치할 수 있거나 같은 경우 값을 올린다.
      start = mid + 1
      res = mid
    else: # 아닌 경우 값을 낮춘다.
      end = mid - 1
  # 정답 반환
  return res

N, C = map(int,input().split())
data = []
for i in range(N):
  data.append(int(input()))
data.sort()

# 탐색 시작
res = search()

# 정답 출력
print(res)