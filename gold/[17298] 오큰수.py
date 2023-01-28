# 2023/01/27 스택
# https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
res = [-1] * N
check = [0] # 인덱스를 담는 리스트.
for i in range(1, N):
  # 체크 안의 인덱스에 해당하는 값보다 큰 값인 경우
  while check and arr[check[-1]] < arr[i]:
    # 체크 안의 값을 pop하여 해당 값으로 지정
    res[check.pop()] = arr[i]
  # 인덱스 추가
  check.append(i)
# 정답 출력
print(*res)