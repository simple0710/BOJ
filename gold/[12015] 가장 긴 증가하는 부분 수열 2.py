# 2022/12/25 DP, 이분탐색
# https://www.acmicpc.net/problem/12015
N = int(input())
data = list(map(int,input().split()))
lis = [0]

# 이분 탐색을 이용한다.
for value in data:
  # 가장 큰 값보다 value가 큰 경우 추가
  if lis[-1] < value:
    lis.append(value)
  else:
    left = 0
    right = len(lis)
    # 이분 탐색
    while left < right:
      mid = (left+right)//2
      if lis[mid] < value:
        left = mid + 1
      else:
        right = mid
    # 증가하는 부분 수열에 맞는 위치에 value를 지정
    lis[right] = value
    
# 정답 출력
print(len(lis) - 1)