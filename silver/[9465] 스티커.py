for _ in range(int(input())):
  n = int(input())
  sticker = [list(map(int,input().split())) for _ in range(2)]
  dp = [list([0] * n) for _ in range(2)]
  if n == 1:
    print(max(sticker[0][0], sticker[1][0]))
    continue
  dp[0][0] = sticker[0][0] 
  dp[1][0] = sticker[1][0]
  dp[0][1] = sticker[0][1] + sticker[1][0]
  dp[1][1] = sticker[1][1] + sticker[0][0]
  # 해당 자리에 들어올 수 있는건
  # [1][i-2], [1][i-1], [0][i-2]
  # 리스트를 그대로 쓰고 [0][i] += max([1][i-2],[1][i-1])으로 적용해도 된다. 
  for i in range(2, n):
    dp[0][i] = max(dp[0][i-2] + sticker[0][i], dp[1][i-2] + sticker[0][i], dp[1][i-1] + sticker[0][i])
    dp[1][i] = max(dp[1][i-2] + sticker[1][i], dp[0][i-2] + sticker[1][i], dp[0][i-1] + sticker[1][i])
    '''
    sticker[0][i] += max([1][i-2], [1][i-1])
    sticker[1][i] == max([0][i-2], [0][i-1])
    '''
  print(max(dp[0][-1],dp[1][-1]))