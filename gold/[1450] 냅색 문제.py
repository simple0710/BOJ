# 2023/02/07 이진 탐색, 중간에서 만나기
# https://www.acmicpc.net/problem/1450
import sys
input = sys.stdin.readline

# 부분합 구하기
def w_search(narr, sumarr, l, w):
  if l >= len(narr):
    sumarr.append(w)
    return
  w_search(narr, sumarr, l + 1, w)
  w_search(narr, sumarr, l + 1, w + narr[l])

# 이진 탐색
def binary_search(arr, start, end, target):
  while start < end:
    mid = (start + end) // 2
    if arr[mid] <= target:
      start = mid + 1
    else:
      end = mid
  return end

N, C = map(int,input().split())
arr = list(map(int,input().split()))
# 절반으로 나누기
left_arr = arr[:N//2]
right_arr = arr[N//2:]
left_sum = []
right_sum = []

w_search(left_arr, left_sum, 0, 0)
w_search(right_arr, right_sum, 0, 0)
right_sum.sort()

res = 0
for i in left_sum:
  if C - i >= 0:
    res += binary_search(right_sum, 0, len(right_sum), C-i)

# 정답 출력
print(res)