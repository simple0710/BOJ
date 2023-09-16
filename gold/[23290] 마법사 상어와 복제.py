# 2023/09/16 Implementation, Simulation
# https://www.acmicpc.net/problem/23290
import sys
input = sys.stdin.readline
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def shark_move_select(eat_cnt, move, x, y): # 상어 경로 탐색
  if len(move) == 3: # 3번 이동을 완료한 경우 먹은 물고기의 수와 경로 반환
    check_list.append([eat_cnt, move])
    return
  for i in range(4):
    nx = x + sdx[i]
    ny = y + sdy[i]
    if 1 <= nx <= 4 and 1 <= ny <= 4:
      v = board[nx][ny]
      board[nx][ny] = 0
      # 해당 위치의 물고기 먹기
      shark_move_select(eat_cnt + v, move+str(i+1), nx, ny)
      board[nx][ny] = v

def solution(shark_x, shark_y, fish_data, S):
  global board, check_list

  fish_smell = [[0] * 5 for _ in range(5)]
  for turn in range(1, S+1):
    # 1. 복제 마법 시전
    copy_data = fish_data[:]

    # 2. 물고기 이동
    board = [[0] * 5 for _ in range(5)]
    new_fish_data = []
    for idx in range(len(fish_data)):
      x, y, d = fish_data[idx]
      for i in range(8):
        nd = (d - i) % 8
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 1 <= nx <= 4 and 1 <= ny <= 4:
          # 상어가 있는 위치, 물고기의 냄새가 있는 칸은 제외한다.
          if (shark_x, shark_y) != (nx, ny) and not fish_smell[nx][ny]:
            new_fish_data.append((nx, ny, nd))
            board[nx][ny] += 1
            break
      else: # 갈 곳이 없는 경우 위치 유지
        board[x][y] += 1
        new_fish_data.append((x, y, d))

    fish_data = new_fish_data

    # 3. 상어 이동
    check_list = []
    # 최적 이동 구하기
    shark_move_select(0, '', shark_x, shark_y)
    # 먹은 물고기(내림차순), 이동 경로(오름차순) 사전순 정렬
    check_list.sort(key=lambda x:(int(x[1])))
    check_list.sort(key=lambda x:(x[0]), reverse=True)
    best = check_list[0] # 최적의 경로
    for i in best[1]:
      i = int(i)-1
      shark_x += sdx[i]
      shark_y += sdy[i]
      if board[shark_x][shark_y]: # 물고기가 있는 경우 냄새 남김
        fish_smell[shark_x][shark_y] = turn
        board[shark_x][shark_y] = 0
    
    # 4. 두 번 전 연습에서 생긴 물고기 냄새 제거
    for i in range(1, 5):
      for j in range(1, 5):
        if turn - fish_smell[i][j] >= 2:
          fish_smell[i][j] = 0

    # 5. 물고기 복제 마법 완료
    new_data = []
    for x, y, d in fish_data:
      if board[x][y]: # 먹히지 않은 물고기 탐색
        new_data.append((x, y, d))
    fish_data = new_data
    fish_data.extend(copy_data)

  return len(fish_data) # 정답 반환

def main():
  M, S = map(int,input().split())
  fish_data = []
  for _ in range(M):
    x, y, d = map(int,input().split())
    fish_data.append((x, y, d-1))
  shark_x, shark_y = map(int,input().split())
  print(solution(shark_x, shark_y, fish_data, S)) # 정답 출력

if __name__ == "__main__":
  main()