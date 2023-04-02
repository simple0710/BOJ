# 2023/04/02 LIS, BinarySearch
# https://www.acmicpc.net/problem/12738
N = int(input())
data = list(map(int,input().split()))
lis = [data[0]]
for v in data:
  if lis[-1] < v: # 마지막 값보다 크다면 추가
    lis.append(v)
  else: # 마지막 값보다 작다면 이진 탐색
    s = 0
    e = len(lis)
    while s < e:
      mid = (s + e) // 2
      if lis[mid] < v:
        s = mid + 1
      else:
        e = mid
    # v보다 크거나 같은위치에 v로 변경
    # abs(v - lis[mid])가 최소가 되는 위치
    lis[e] = v
# 정답 출력
print(len(lis))