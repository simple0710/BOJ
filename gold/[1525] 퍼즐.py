# 2022/11/02 너비우선탐색, 딕셔너리
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # 이동된 상태 저장
  q = deque()
  q.append(start)

  # 현재 상태, 이동 횟수 저장(초기 상태)
  cnt_dict = dict()
  cnt_dict[start] = 0

  while q:
    now = q.popleft()

    # 정리가 완료 됐을 경우 이동횟수 반환
    if now == "123456789":
      return cnt_dict[now]
    
    # 빈 공간의 열과 행을 구한다.
    pos = now.find("9")
    x = pos // 3
    y = pos % 3

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 3 and 0 <= ny < 3:
        # 이동할 위치
        n_pos = nx * 3 + ny
        # 이동된 상태 설정
        next_num = list(now)
        next_num[n_pos], next_num[pos] = next_num[pos], next_num[n_pos]
        next_num = "".join(next_num)

        # cnt_dict 이 next_num을 가지지 않은 경우
        # visited와 같은 역할
        if not cnt_dict.get(next_num):
          # 이동된 상태 저장, 이동횟수 + 1
          q.append(next_num) # next_num 추가
          cnt_dict[next_num] = cnt_dict[now] + 1
          
if __name__ == "__main__":
  start = ""
  for i in range(3):
    # 123456780 형태로 변환
    temp = sys.stdin.readline().strip()
    temp = temp.replace(" ", "")
    start += temp

  start = start.replace("0", "9")

  result = bfs(start)

  # 이동이 불가한 경우 "-1" 출력
  if result != None:
    print(result)
  else:
    print("-1")