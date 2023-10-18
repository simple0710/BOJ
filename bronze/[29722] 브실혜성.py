# 2023/09/10 Math, Implementation
# https://www.acmicpc.net/problem/29722
import sys
input = sys.stdin.readline

def solution(N):
  y = N // 360 # 년
  N %= 360
  m = N // 30 # 월
  N %= 30
  now[0] += y # 연도 추가
  if now[2]+N <= 30: # 30일 이하인 경우
    now[2] = now[2] + N
  else: # 30일 초과인 경우
    now[2] = (now[2]+N)%30
    now[1] += 1 # 1달 추가

  if now[1]+m <= 12: # 12달 이하인 경우
    now[1] = now[1] +  m
  else: # 12달 초과인 경우
    now[1] = (now[1]+m) % 12
    now[0] += 1 # 1년 추가
  for i in range(3): # 정답 형 변환
    if now[i] < 10:
      now[i] = f'0{now[i]}'
  # 정답 출력(yyyy-mm-dd)
  print('-'.join(map(str, now)))

if __name__ == "__main__":
  now = list(map(int,input().split('-')))
  N = int(input())
  solution(N) # 코드 실행