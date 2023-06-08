# 2023/06/08 Geometry
# https://www.acmicpc.net/problem/1297
D, H, W = map(int,input().split())
r = D / (H**2 + W**2) ** 0.5 # 비율 구하기
# 정답 출력
print(int(H * r), int(W * r))