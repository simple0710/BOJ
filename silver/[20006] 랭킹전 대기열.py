# 2023/10/19 Implemenatation, Simulation
# https://www.acmicpc.net/problem/20006
import sys
inpuut = sys.stdin.readline

def solution(P, M, player):
  rooms = []
  for name in player:
    for i in range(len(rooms)):
      if len(rooms[i]) < M: # 방의 정원이 M 미만인 경우
        # 처음 입장한 플레이어의 레벨 기준 차이가 10이하라면 입장이 가능하다. 
        if abs(player[rooms[i][0]] - player[name]) <= 10:
          rooms[i].append(name)
          break
    else: # 방에 입장하지 못한 경우 새로운 방을 만든다.
      rooms.append([name])

   # 정답 출력
  for room in rooms:
    room.sort() # 이름을 오름차순으로 정렬
    # 시작 여부, 방의 인원 출력
    print("Started!" if len(room) == M else "Waiting!")
    for name in room:
      print(player[name], name)

def main():
  # 플레이어의 수, 방의 정원
  P, M = map(int,input().split())
  # 플레이어 정보
  player = dict()
  for _ in range(P):
    level, name = input().rstrip().split()
    player[name] = int(level)
  solution(P, M, player) # 코드 실행

if __name__ == '__main__':
  main()