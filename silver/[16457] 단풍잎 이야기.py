# 2022/12/17 백트래킹
# https://www.acmicpc.net/problem/16457
def dfs(start, depth):
  global res
  if depth == N:
    p = 0
    # 모든 퀘스트를 확인
    for quest in quests:
      plus = 1
      for j in quest:
        # 못깨는 퀘스트면 plus = 0
        if j not in s:
          plus = 0
          break
      p += plus
    res = max(p, res)
    return
  
  for i in range(start, len(total_skill)):
    if total_skill[i] not in s:
      s.append(total_skill[i])
      dfs(i, depth+1)
      s.pop()

if __name__ == "__main__":
  N, M, K = map(int,input().split())
  total_skill = set()
  quests = []
  for i in range(M):
    a = list(map(int,input().split()))
    for i in a:
      total_skill.add(i)
    quests.append(a)
  total_skill = sorted(list(total_skill))

  res = 0
  s = []
  # 백트래킹 시작
  dfs(0, 0)

  # 모든 스킬 수가 N보다 작다면 모든 퀘스트를 깰 수 있다.
  if len(total_skill) <= N:
    print(M)
  else:
    print(res)