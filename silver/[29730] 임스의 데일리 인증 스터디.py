# 2023/09/10 String, Sorting, Parsing
# https://www.acmicpc.net/problem/29730
import sys
input = sys.stdin.readline

def solution():
  data.sort() # 기록 정렬
  data.sort(key=lambda x:len(x)) # 길이 순 정렬
  next = []
  for i in data:
    # 백준 문제인 경우
    if len(i) >= 6 and i[:6] == 'boj.kr':
      next.append(i)
    else: # 백준 문제가 아니면 바로 출력
      print(i)
  for i in next: # 백준 문제 기록 출력
    print(i)

if __name__ == "__main__":
  # 공부 기록의 개수
  N = int(input())
  # 공부 기록 입력
  data = [input().rstrip() for _ in range(N)]
  solution() # 코드 실행