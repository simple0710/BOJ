# 2023/02/14 그리디
# https://www.acmicpc.net/problem/2885
K = int(input())
two = []
p = 1
# 초콜릿 크기는 K보다는 커야 한다.
while p < K:
  p *= 2

ans1 = p
ans2 = 0
while True:
  # 나누어지는 경우 종료
  if K % p == 0:
    break
  else: # 절반으로 나누기
    p //= 2
    ans2 += 1

# 정답 출력
print(ans1, ans2)