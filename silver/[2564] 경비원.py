import sys
input = sys.stdin.readline

# 상대 거리보다 절대거리를 계산해보자
def get_distance(x, y):
  if x == 1: # 북
    return y
  if x == 2: # 남
    return w + h + w - y
  if x == 3: # 서
    return w + h + w + h - y
  if x == 4:
    return w + y # 동

w, h = map(int,input().split()) # 가로 세로
shop_cnt = int(input())# 상점의 개수

course = list()
for i in range(shop_cnt + 1):
  a, b = map(int,input().split()) # 방향, 거리
  course.append(get_distance(a, b))

result = 0
for i in range(shop_cnt):
  # 전체 길이에서 인코스를 빼면 아웃코스
  in_course = abs(course[-1] - course[i])
  out_course = 2 * (w + h) - in_course
  result += min(in_course, out_course)

print(result)