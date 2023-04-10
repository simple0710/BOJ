# 2023/04/10 Implementation, BinarySearch
# https://www.acmicpc.net/problem/16434
import sys, math
input = sys.stdin.readline

def moves(mid_value):
  na = ATK
  hp = mid_value
  for t, a, h in room:
    if t == 1: # 몬스터 전투
      atk_cnt = math.ceil(h / na) # 용사의 공격 횟수
      hp -= a * (atk_cnt - 1) # 용사 생명력 감소
    else: # 포션
      na += a
      hp += h
      if hp > mid_value:
        hp = mid_value
    if hp <= 0: # 용사 사망
      return False
  return True

def binary_search():
  s = 0
  e = sys.maxsize
  res = sys.maxsize
  while s <= e:
    mid = (s + e) // 2
    check = moves(mid)
    if check: # 끝까지 도착한 경우
      res = min(res, mid)
      e = mid - 1
    else: # 끝까지 도착하지 못한 경우
      s = mid + 1
  # 정답 반환
  return res

N, ATK = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
# 탐색 시작
res = binary_search()
# 정답 출력
print(res)