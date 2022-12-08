# 2022/12/04 백트래킹?
# https://www.acmicpc.net/problem/15663
# 해결 방법 1
# 순열을 생성, 중복을 제거, 정렬을 한 후에 출력한다.
def solution1():
  from itertools import permutations

  N, M = map(int,input().split())
  arr = list(map(int,input().split()))
  res = set(permutations(arr, M))
  res = sorted(list(res))
  for i in res:
    print(*i)

# 해결방법 2
# 방문 리스트를 만들고 확인, res가 이미 있다면 추가하지 않는다.
def solution2():
  def back():
    if len(s) == M:
      tmp = ' '.join(map(str, s))
      if tmp not in res:
        res.append(tmp)
      return
    for i in range(N):
      if not visited[i]:
        visited[i] = True
        s.append(arr[i])
        back()
        visited[i] = False
        s.pop()

  N, M = map(int,input().split())
  arr = list(map(int,input().split()))
  arr.sort()
  s = []
  res = []
  visited = [False] * N
  back()
  for i in res:
    print(i)
