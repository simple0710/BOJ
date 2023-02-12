# 2023/02/12 BruteForce
# https://www.acmicpc.net/problem/16637
import sys
input = sys.stdin.readline

# 연산 처리
def cal(a, b, c):
  a = int(a)
  b = int(b)
  if c == '+':
    return a + b
  if c == '-':
    return a - b
  if c == '*':
    return a * b

def dfs(idx, s): # 인덱스, 현재 값
  global ans
  if idx == N - 1: # 더 이상 계산할 수 없는 경우 max값 비교
    ans = max(ans, s)
    return
  if idx + 2 < N: # 평범한 계산
    s1 = cal(s, data[idx+2], data[idx+1])
    dfs(idx + 2, s1)
  if idx + 4 < N: # 괄호 치기
    s2 = cal(s, cal(data[idx+2], data[idx+4], data[idx+3]), data[idx+1])
    dfs(idx + 4, s2)

N = int(input())
data = list(input().rstrip())
ans = -(sys.maxsize)

# 탐색 시작
dfs(0, int(data[0]))

# 정답 출력
print(ans)