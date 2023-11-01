# 2023/06/21 DataStructures, BinarySearch, Sorting, Greedy, PriorityQueue
# https://www.acmicpc.net/problem/17503
import sys, heapq
input = sys.stdin.readline

def priotiry_queue():
  # 도수 레벨 오름차순 정렬
  beer.sort(key=lambda x: x[1])
  pick = []
  check = 0
  for i in range(K):
    v, c = beer[i]
    # 도수가 작은 맥주부터 선택
    heapq.heappush(pick, (v, c))
    check += v
    # 마시는 맥수가 N개인 경우
    if len(pick) == N:
      if check >= M: # 선호도가 M 이상인 경우
        print(c) # 레벨의 최솟값 출력
        exit()
      else:
        # 레벨 감소
        check -= heapq.heappop(pick)[0]
  else:
    print(-1)

def binary_search():
  MAX = max([i[1] for i in beer]) + 1
  res = MAX
  s = 1
  e = MAX 
  while s <= e:
    mid = (s + e) // 2 # 간 레벨 계산
    check = []
    for v, c in beer:
      # 1. 맥주 도수 레벨 > 간 레벨 == 기절
      if c <= mid:
        check.append(v)
    check.sort(reverse=True)
    # 2. N일 동안 먹을 수 있는 경우 and 마시는 맥주의 선호도 합 >= M
    if len(check) >= N and sum(check[:N]) >= M:
      res = min(res, mid)
      e = mid - 1
    else:
      s = mid + 1
  # 정답 출력
  print(res if res != MAX else -1)

# 기간, 선호도 합, 종류
N, M, K = map(int,input().split())
# 도수 레벨의 최솟값 구하기
beer = []
for _ in range(K):
  v, c = map(int,input().split())
  beer.append((v, c))
# 탐색 시작
# binary_search()
# priotiry_queue()