# 2023/08/15 Math, Implementation, Ad-Hoc, Probability
# https://www.acmicpc.net/problem/28682
import sys
input = sys.stdin.readline
flush = sys.stdout.flush

N = int(input())
ans = ''
# 전부 축구로 선택한다.
print('soccer' + ' soccer' * (N - 1))
flush()
# 과목을 입력 받는다.
res = input().rstrip().split()
flush()
for i in res:
  if i == 'swimming': # 수영이 나오면 볼링을 선택한다.
    ans += 'bowling '
  else: # 볼링이 나오면 수영을 선택한다.
    ans += 'swimming '
print(ans) # 정답 출력
flush()