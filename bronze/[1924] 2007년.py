# 2023/05/16 Math, Implementation
# https://www.acmicpc.net/problem/1924
d = 0
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w = ['SUN', "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int,input().split())

for i in range(x - 1):
  d += m[i]
# 요일 구하기
d = (d + y) % 7
# 정답 출력
print(w[d])