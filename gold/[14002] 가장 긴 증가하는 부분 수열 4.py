# 2022/11/26 DP
# 정보 입력
N = int(input())
arr = list(map(int,input().split()))
dp = [1] * N
# 한 지역과 그 이전 지역을 탐색
for i in range(N):
  for j in range(i):
    # 만약 자신보다 수가 작다면 비교한다.
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

# 최장 수열의 크기
check = max(dp)

dp_list = []
# 뒤에서 부터 확인
for i in range(N-1, -1, -1):
  # 최장 길이와 check가 같다면 다른 리스트에 추가 후 check -= 1을 수행한다.
  if dp[i] == check:
    dp_list.append(arr[i])
    check -= 1
    
# 반대로 돌린다.
dp_list.reverse()

# 정답 출력
print(max(dp))
print(' '.join(map(str, dp_list)))