n = int(input())

nums = [1] * 10
for _ in range(n-1):
  for i in range(1, 10):
    # 맨 끝에 0이 온다면 이전엔 0만 올 수 있고,
    # 맨 끝에 1이 온다면 이전엔 0, 1이 올 수 있고,
    # 맨 끝에 2가 온다면 이전엔 0, 1, 2가 올 수 있다.
    # 그러므로 맨 끝에 i가 온다면 nums[i] + nums[i-1]이다.
    nums[i] = (nums[i] + nums[i - 1]) % 10007

# 0 ~ 9의 수가 맨 끝에 온 경우의 수의 합 % 10007
print(sum(nums)%10007)