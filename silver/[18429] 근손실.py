# 2023/11/17 Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/18429
import sys
input = sys.stdin.readline

def back(total):
  global res
  if total < 500: # 중량이 500 미만이면 종료
    return
  if len(s) == N: # 모든 운동 키트를 적용한 경우
    res += 1
    return
  for i in range(N):
    if i not in s: # 중복되지 않는 숫자를 선택한다.
      s.append(i)
      # 총 중량 - 감소하는 중량
      back(total + kit[i] - K)
      s.pop()

# 운동 키트의 개수, 감소하는 중량
N, K = map(int,input().split())
# 운동 키트 정보
kit = list(map(int,input().split()))
s = []
res = 0
back(500) # 탐색 시작
# 경우의 수 출력
print(res)