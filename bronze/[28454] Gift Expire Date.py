# 2023/08/12 Implementation, String
# https://www.acmicpc.net/problem/28454
now_day = list(map(int,input().split('-')))
N = int(input())
res = 0
for _ in range(N):
  check_day = list(map(int,input().split('-')))
  if now_day[0] < check_day[0]: # 연도가 지나지 않은 경우
    res += 1
  elif now_day[0] == check_day[0]: # 연도가 같은 경우
    if now_day[1] < check_day[1]: # 월이 지나지 않은 경우
      res += 1
    elif now_day[1] == check_day[1]: # 월이 같은 경우
      if now_day[2] <= check_day[2]: # 일이 지나지 않은 경우
        res += 1
print(res) # 사용할 수 있는 기프티콘의 개수 출력