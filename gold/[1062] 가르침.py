# 2022/12/12 백트래킹
# https://www.acmicpc.net/status?user_id=simple710&problem_id=1062&from_mine=1
import sys
input = sys.stdin.readline

def back(start, depth):
  global res
  # 외울 수 있는 만큼 외운 경우
  if depth == K - 5:
    p = 0
    # 단어 확인
    for word in words:
      flag = 1
      for j in word:
        # 단어가 방문처리 되지 않은 경우 종료
        if not visited[ord(j) - ord('a')]:
          flag = 0
          break
      if flag:
        p += 1
    res = max(p, res)
    return
    
  # 알파벳 전 지역 탐색
  for i in range(start, 26):
    if not visited[i]:
      visited[i] = True
      back(i, depth + 1)
      visited[i] = False

N, K = map(int,input().split())
if K < 5: # 알파벳이 5개 이하인 경우 단어를 외우지 못한다.
  print(0)
  exit()
elif K == 26: # 26개인 경우 모든 단어를 외울 수 있다.
  print(N)
  exit()

# 단어 입력
words = [set(input().strip()[4:-4]) for _ in range(N)]
visited = [False] * 26 # 알파벳 리스트 생성
# 기본으로 알아야 할 것들 True값으로 지정
for i in ('a', 'c', 'i', 'n', 't'):
  visited[ord(i)-ord('a')] = True
res = 0
back(0, 0) # 백트래킹
print(res) # 정답 출력