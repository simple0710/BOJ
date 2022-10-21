import sys
input = sys.stdin.readline

word_1 = ' ' + input().rstrip()
word_2 = ' ' + input().rstrip()

length_1 = len(word_1)
length_2 = len(word_2)
dp = [[0] * length_2 for _ in range(length_1)]

for i in range(1, length_1):
  for j in range(1, length_2):
    # 문자가 같은 경우
    if word_1[i] == word_2[j]:
      # 이전 LCS 길이에 +1이 된다.
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

print(dp[-1][-1])