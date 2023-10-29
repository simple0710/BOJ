# 2023/10/28 Greedy
# https://www.acmicpc.net/problem/30404
import sys
input = sys.stdin.readline

def main():
  # 소리 내는 횟수, 박수를 안 쳐도 되는 구간
  N, K = map(int,input().split())
  # 소리를 내는 시각 정보
  duck_sound_time = list(map(int,input().split()))
  s = 0 # 처음 박수를 친 시점
  res = 1 # 박수를 친 횟수
  for i in range(1, N):
    # 처음 박수 친 시점과 현재 시점의 차이가 K 초과인 경우
    if duck_sound_time[i] - duck_sound_time[s] > K:
      # 시점 갱신 및 박수 횟수 추가
      s = i
      res += 1
  # 최소 박수 횟수 출력
  print(res)

if __name__ == "__main__":
  main()