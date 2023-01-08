# 2023/01/08 이진 탐색
# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline

# 이진 탐색
def binary_search(start, end, value):
  while start <= end:
    mid = (start + end) // 2
    # 중간 값이 현재 값보다 크다면 end 값은 mid - 1
    if arr1[mid] > value:
      end = mid - 1
    # 중간 값이 현재 값보다 작다면 start 값은 mid + 1
    elif  arr1[mid] < value:
      start = mid + 1
    # 중간 값이 현재 값이랑 같다면 True 반환
    else:
      return True

if __name__=="__main__":
  N = int(input())
  arr1 = sorted(list(map(int,input().split())))
  M = int(input())
  arr2 = list(map(int,input().split()))

  res = []
  for i in arr2:
    if binary_search(0, N-1, i):
      res.append(1)
    else:
      res.append(0)
  
  # 정답 출력
  print(*res)