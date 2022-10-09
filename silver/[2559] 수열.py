import sys
input = sys.stdin.readline

n, k = map(int,input().split())
data = list(map(int,input().split()))

result = list()
result.append(sum(data[:k]))

# :k까지 더한 값에 맨 앞의 값을 뺀 후 뒤에 갚은 더하면 i:k의 범위를 구할 수 있다.
# ex
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# 시작 값은 -1, 다음 값은 시작 값 -1 에서 맨 앞인 3을 뻬고 -4를 더한다.
for i in range(n - k):
  result.append(result[i] - data[i] + data[k + i])

print(max(result))