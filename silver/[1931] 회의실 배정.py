import sys
input = sys.stdin.readline

t = int(input())
data = [[0] * 2 for _ in range(t)]
for i in range(t):
  x, y = map(int,input().split())
  data[i][0] = x
  data[i][1] = y
# 먼저 끝나는 시간을 기준으로 정렬
# 그 다음 시작하는 시간 순으로 정렬
# 하단 순서대로 진행
# data.sort(key = lambda x : x[1])
# data.sort(key = lambda x : x[0])
data.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = data[0][1]
for i in range(1, t):
  # 시작하는 시간보다 끝나는 시간이 작거나 같은 경우
  # (시간이 겹치지 않는 경우)
  # cnt += 1, 끝나는 시간 변경
  if data[i][0] >= end_time:
    cnt += 1
    end_time = data[i][1]
print(cnt)