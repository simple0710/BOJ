# 2023/03/17 Prefix Sum
# https://www.acmicpc.net/problem/16139
import sys
input = sys.stdin.readline

word = input().rstrip()
dic = {}
dic[-1] = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
for i in range(len(word)): # 누적 합 계산
  dic[i] = dic[i-1].copy()
  dic[i][word[i]] += 1

for _ in range(int(input())):
  q = input().split()
  # 정답 출력
  print(dic[int(q[2])][q[0]] - dic[int(q[1])-1][q[0]])