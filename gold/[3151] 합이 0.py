# 2023/11/28 Brutforcing, Sorting, BinarySearch, TwoPointer
# https://www.acmicpc.net/problem/3151
import sys
input = sys.stdin.readline

def binary_search(v):
  s = 0
  e = N-1
  while s < e:
    mid = (s + e) // 2
    if data[mid] < v:
      s = mid + 1
    else:
      e = mid
  return e # 인덱스 반환

def two_pointer(now):
  s = now+1
  e = N-1
  cnt = 0
  while s < e:
    total = data[now] + data[s] + data[e]
    if total <= 0: # 0보다 작거나 같으면 s증가
      if total == 0: # 0과 같다면 경우 확인
        if data[s] == data[e]: # 같은 수인 경우 중복되는 개수만큼 추가
          cnt += e - s
        else: # 다른 수인 경우 오른쪽의 수에서 가장 왼쪽의 인덱스를 구한다.
          idx = binary_search(data[e])
          cnt += e - idx + 1
      s += 1
    else: # 0보다 크다면 e 감소
      e -= 1
  return cnt # 경우의 수 반환

def solution():
  res = 0
  for i in range(N-2):
    res += two_pointer(i) # i부터 N까지 탐색 시작
  return res # 경우의 수 반환

def main():
  global N, data
  N = int(input())
  data = sorted(list(map(int,input().split())))
  print(solution()) # 경우의 수 출력

if __name__ == "__main__":
  main()