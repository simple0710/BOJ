from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  c = input() # 커맨드, RDD
  length = int(input()) # 리스트 길이
   # "[", "]", ","를 제외한 큐 생성
  result_list = deque(input().rstrip()[1:-1].split(","))
  flag = 0 # 에러 여부 확인
  cnt = 0 # R 횟수 체크

  if length == 0:
    result_list = []

  # 커맨드 실행
  for i in c:
    if i == "R":
      cnt += 1
    elif i == "D":
      # 빈 리스트인 경우 에러 출력
      if len(result_list) == 0:
        flag = 1
        print("error")
        break
      else:
        # R 횟수에 따른 pop() 실행
        if cnt % 2 == 0:
          result_list.popleft()
        else:
          result_list.pop()

  if flag == 0:
    if cnt % 2 != 0:
      result_list.reverse()
    print("["+",".join(result_list) + "]")