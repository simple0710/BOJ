# 2023/10/18 Greedy
# https://www.acmicpc.net/problem/2138
import sys
input = sys.stdin.readline
MAX = sys.maxsize

def check(N, s, e):
  ns = s[:]
  cnt = 0
  for i in range(1, N):
    if ns[i-1] != e[i-1]: # 왼쪽 전구가 최종 결과와 같지 않은 경우
      # i번 전구 상태 변경.
      cnt += 1
      for j in range(i-1, i+2): # 주변 전구
        if j < N:
          ns[j] = 1 - ns[j]
  if ns == e: # 결과와 같다면 cnt 반환
    return cnt
  else: # 결과와 다르다면 MAX 반환
    return MAX

def solution(N, s, e):
  # 1. 왼쪽 전구를 키지 않고, 나머지 전구를 확인한다.
  res = check(N, s, e)
  # 2. 왼쪽 전구를 키고, 나머지 전구를 확인한다.
  s[0] = 1 - s[0]
  s[1] = 1 - s[1]
  res = min(res, check(N, s, e) + 1) # 둘을 비교해서 작은 값을 정답으로 한다.
  if res != MAX: # 정답이 MAX가 아니라면 최소값 반환
    return res
  else: # 정답이 MAX인 경우 -1 반환
    return -1

def main():
  N = int(input())
  # 시작 상태
  s = list(map(int, input().rstrip()))
  # 최종 상태
  e = list(map(int, input().rstrip()))
  print(solution(N, s, e)) # 버튼을 최소로 누르는 횟수 출력

if __name__ == "__main__":
  main()