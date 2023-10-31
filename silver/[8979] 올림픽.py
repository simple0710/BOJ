# 2023/10/31 Implementation, Sorting
# https://www.acmicpc.net/problem/8979
import sys
input = sys.stdin.readline

def solution(N, K, data):
  # 금, 은, 동 순으로 정렬
  data.sort(key=lambda x:(-x[1], -x[2], -x[3]))
  rank = 0
  before = data[0][1:]
  for idx in range(N):
    if data[idx][1:] != before: # 이전 값과 다르다면 순위 갱신
      rank = idx
      before = data[idx][1:]
    # 구하고자 하는 등수인 경우
    if data[idx][0] == K: return rank + 1

def main():
  # 국가의 수, 구하고자 하는 국가 K
  N, K = map(int,input().split())
  # 국가별 메달 현황
  nation_medal_list = [list(map(int,input().split())) for _ in range(N)]
  # K 국가의 순위 출력
  print(solution(N, K, nation_medal_list))

if __name__ == "__main__":
  main()