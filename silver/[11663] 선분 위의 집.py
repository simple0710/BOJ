# 2023/07/12 Sorting, BianrySearch
# https://www.acmicpc.net/problem/11663
import sys
input = sys.stdin.readline

def binary_search_s(): # 시작점 확인
  s = 0
  e = N - 1
  check = N
  while s <= e:
    mid = (s + e) // 2
    if point[mid] >= sp:
      check = min(mid, check)
      e = mid - 1
    else:
      s = mid + 1
  return check

def binary_search_e(): # 끝점 확인
  s = 0
  e = N - 1
  check = -1
  while s <= e:
    mid = (s + e) // 2
    if point[mid] <= ep:
      check = max(mid, check)
      s = mid + 1
    else:
      e = mid - 1
  return check

N, M = map(int,input().split())
point = sorted(list(map(int, input().split())))
for _ in range(M):
  # 시작점, 끝점
  sp, ep = map(int,input().split())
  # 정답 출력
  print(binary_search_e() - binary_search_s() + 1)