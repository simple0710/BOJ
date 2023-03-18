# 2023/03/18 Greedy
# https://www.acmicpc.net/problem/2785
N = int(input())
chain = sorted(list(map(int,input().split())))
cnt = 1
for c in chain:
  if cnt + c >= N: # 채운 공간 + 현재 체인 >= 체인 개수
    break
  else:
    cnt += c # 공간 채우기
    N -= 1 # 남은 공간 -1
# 정답 출력
print(N-1)