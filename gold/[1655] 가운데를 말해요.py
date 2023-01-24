# 2023/01/24 우선순위 큐
# https://www.acmicpc.net/problem/1655
import heapq, sys
input = sys.stdin.readline

N = int(input())
left_heap = [] # 중간 값보다 작은 값
right_heap = [] # 중간 값보다 큰 값
for i in range(N):
  num = int(input())
  # 값을 번갈아가며 추가해준다.
  if len(left_heap) == len(right_heap):
    heapq.heappush(left_heap, -num)
  else:
    heapq.heappush(right_heap, num)
  
  '''
   -left_heap[0]은 가장 작은 값을 출력한다.
   따라서 right_heap[0]에 가장 작은 값이 들어간다면 위치를 바꿔준다.
  '''
  if right_heap and right_heap[0] < -left_heap[0]:
    l = heapq.heappop(left_heap)
    r = heapq.heappop(right_heap)

    heapq.heappush(left_heap, -r)
    heapq.heappush(right_heap, -l)
  # 정답 출력
  print(-left_heap[0])