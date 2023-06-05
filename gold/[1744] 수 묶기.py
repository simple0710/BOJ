# 2023/06/03 Greedy, Sorting
# https://www.acmicpc.net/problem/1744
N = int(input())
data_p = []
data_m = []
for _ in range(N):
  v = int(input())
  # 양수, 음수 분류
  if v > 0:
    data_p.append(v)
  else:
    data_m.append(v)
# 내림차 순으로 정렬
data_p.sort(reverse=True)
data_m.sort()
res = 0
for i in range(1, len(data_p), 2): # 양수의 경우
  # 1 + 1이나, 1 * 1의 경우 고려
  res += max(data_p[i] * data_p[i-1], data_p[i] + data_p[i-1])
for i in range(1, len(data_m), 2):
  res += data_m[i] * data_m[i-1]

# 짝이 맞지 않는 경우 마지막 값을 더한다.
if len(data_p) % 2 != 0:
  res += data_p[-1]
if len(data_m) % 2 != 0:
  res += data_m[-1]

# 정답 출력
print(res)