# 2023/09/10 SlidingWindow
# https://www.acmicpc.net/problem/29718
import sys
input = sys.stdin.readline

def solution():
  arr = []
  for i in range(M): # 각 열을 확인한다.
    # 행의 합을 추가한다.
    arr.append(sum([clap[j][i] for j in range(N)]))
  res = 0
  for i in range(M-choice+1):
    # 현재 위치에서 선택지 수만큼 확인
    res = max(res, sum(arr[i:i+choice]))
  # 가장 많이 박수를 친 구간의 박수 횟수 출력
  print(res)

if __name__ == "__main__":
  # 행, 열
  N, M = map(int,input().split())
  # 박수 정보 입력
  clap = []
  for _ in range(N):
    clap.append(list(map(int,input().split())))
  # 선택 수
  choice = int(input())
  solution() # 코드 실행