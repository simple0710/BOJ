import sys
input = sys.stdin.readline

finish = int(input())
b_n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_cnt = abs(100 - finish)

# 50000제한인데 1000001인 이유
# 400 에서 500 가는 것보다 550에서 500을 가는 것이 더 빠르다.
for nums in range(1000001):
  nums = str(nums)
  for j in range(len(nums)):
    # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
    if int(nums[j]) in broken:
      break
    # 고장난 숫자 없이 마지막자리까지 왔다면 min_cnt 비교 후 업데이트
    elif j == len(nums) - 1:
      min_cnt = min(min_cnt, abs(int(nums) - finish) + len(nums))

print(min_cnt)