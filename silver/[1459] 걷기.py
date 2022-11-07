# 2022/11/07 그리디 알고리즘
# 정보 입력
X, Y, W, S = map(int,input().split())

# W(직선 x)로만 이동
res1 = (X+Y) * W

# 대각선으로만 도착할 수 있는 경우
if (X+Y) % 2 == 0:
  res2 = max(X, Y) * S
# 대각선으로만 도착할 수 없는 경우
else:
  res2 = (max(X, Y) - 1) * S + W

# S와 W로 움직인 경우
res3 = (min(X,Y) * S) + (abs(X-Y) * W)

# 정답 출력
print(min(res1, res2, res3))