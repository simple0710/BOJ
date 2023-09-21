# 2023/06/24 BinarySearch
# https://www.acmicpc.net/problem/1477
def binary_search():
  s = 1
  e = L - 1
  while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(1, N + 2):
      cnt += (track[i] - track[i-1] - 1) // mid
    if cnt > M: # M개 초과로 설치하는 경우
      s = mid + 1
    else: # M개 이하로 설치하는 경우
      res = mid # M개 미만인 경우 아무 곳에 M - cnt만큼 설치
      e = mid - 1
  # 정답 출력
  print(res)

N, M, L = map(int,input().split())
track = [0] + sorted(list(map(int,input().split()))) + [L]
# 탐색 시작
binary_search()