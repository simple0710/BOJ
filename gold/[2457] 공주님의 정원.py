# 2023/11/27 Greedy, Sorting
# https://www.acmicpc.net/problem/2457
# 날짜 일 수 구하기
def check_date():
  month = [0] * 13
  for i in range(1, 13):
    v = 31
    if i in [2]:
      v = 28
    elif i in [4, 6, 9, 11]:
      v = 30
    month[i] = month[i-1] + v
  return month

def solution(N, data):
  # 데이터 정렬
  data.sort()
  before = 0
  cnt = 0
  check = 0
  month = check_date()
  for s_month, s_date, e_month, e_date in data:
    # 3월 1일 이전인 경우를 확인한다.
    if month[s_month-1] + s_date <= month[2] + 1:
      check = max(check, month[e_month-1] + e_date)
      # 12월까지 피게한 경우 1을 반환한다.
      if e_month == 12:
        return 1
      continue
    # 이전에 피웠던 꽃이 지는 시기보다 더 늦게 피는 경우
    if month[s_month-1] + s_date > before:
      if not check: # 이전에 선택한 꽃이 없는 경우 종료한다.
        return 0
      # 이전에 선택했던 꽃을 선택한다.
      before = check
      check = 0
      cnt += 1
    # 이전에 피웠던 꽃보다 피는 시기가 작은 경우를 확인한다.
    if month[s_month-1] + s_date <= before:
      # 가장 오래 피는 꽃을 선택한다.
      check = max(check, month[e_month-1] + e_date)
      # 12월까지 피게한 경우 피운 꽃의 개수를 반환한다.
      if e_month == 12:
        return cnt + 1
  return 0

def main():
  N = int(input())
  data = [list(map(int,input().split())) for _ in range(N)]
  print(solution(N, data)) # 선택한 꽃들의 최소 개수를 출력

if __name__ == "__main__":
  main()