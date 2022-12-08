# 2022/11/28 그리디 알고리즘
# 정보 입력
N = int(input())
data = []
for _ in range(N):
  data.append(int(input()))

# 탐색 시작
cnt = 0
# 정답 1
# 맨 뒤에서 부터 확인
for i in range(N-1, 0, -1):
  # 만약 더 작거나 같다면 수를 줄임
  if data[i-1] >= data[i]:
    cnt += data[i-1] - data[i] + 1
    data[i-1] = data[i] - 1

# 정답 2
# for i in range(N-1, 0, -1):
#   while data[i] <= data[i-1]:
#     data[i-1] -= 1
#     cnt += 1

# 정답 출력
print(cnt)