# 2023/10/27 Impelmentation
# https://www.acmicpc.net/problem/20125
import sys
input = sys.stdin.readline

def find_down(N, data, x, y): # 몸, 다리 길이 구하기
  cnt = 0
  for i in range(x, N):
    if data[i][y] != '*': # 신체가 아닌 경우
      break
    cnt += 1
  return cnt # 길이 반환

def solution(N, data):
  for i in range(N-3): # 머리가 있을 수 있는 최대 행 크기
    if '*' in data[i]: # 머리가 있는 경우
      x, y = i+1, data[i].index('*') # 심장 위치
      left_arm = y - data[x].index('*') # 왼쪽 팔
      right_arm = N - data[x][::-1].index('*') - 1 - y # 오른쪽 팔
      body = find_down(N, data, x+1, y) # 허리
      left_leg = find_down(N, data, x+body+1, y-1) # 왼쪽 다리
      right_leg = find_down(N, data, x+body+1, y+1) # 오른쪽 다리
      # 정답 출력
      # 심장 위치
      # 왼쪽 팔, 오른족 팔, 허리, 왼쪽 다리, 오른쪽 다리
      print(x+1, y+1)
      print(left_arm, right_arm, body, left_leg, right_leg)
      return

def main():
  # 한 변의 길이
  N = int(input())
  # 정각형 판 상태
  data = [list(input().rstrip()) for _ in range(N)]
  solution(N, data) # 코드 실행

if __name__ == "__main__":
  main()