import sys

input = sys.stdin.readline
n = int(input()) # 크레인 수
crane = list(map(int,input().split())) # 무게 제한
m = int(input()) # 박스의 수
box = list(map(int,input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

# 가장 큰 박스를 들 수 없다면 -1 후 종료
if box[0] > crane[0]:
  print(-1)
  sys.exit()
else:
  time = 0
  while box:
    if not box:
      break
    for i in crane:
      for j in box:
        if i >= j:
          box.remove(j)
          break
    time += 1        
print(time)

''' 이진탐색 시간 초과
box.sort()
def binary(box, start, end, target):
  if start > end:
    return None
  my_box = None
  while start <= end:
    mid = (start + end) // 2
    if box[mid] == target:
      return target
    elif box[mid] > target:
      end = mid - 1 
    elif box[mid] < target:
      my_box = box[mid]
      start = mid + 1
  return my_box
'''