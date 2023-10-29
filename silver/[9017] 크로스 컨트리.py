# 2023/10/29 Implementation, DataStructures, Sorting
# https://www.acmicpc.net/problem/9017
from collections import defaultdict
import sys
input = sys.stdin.readline

# 인원이 6명인지 확인
def check_six(data):
  six_team = defaultdict(int)
  for i in data:
    six_team[i] += 1
  # 6명이 있는 팀만으로 운동 경기를 한 경우 반환
  return [i for i in data if six_team[i] == 6]

# 점수 확인 및 랭킹 반환
def check_score(rank):
  team = defaultdict(list)
  for i in range(len(rank)):
    team[rank[i]].append(i+1)
  # 랭킹과 팀 순위를 저장한 배열 저장 
  new_data = [[i] + team[i] for i in team]
  # 순위 정렬, 점수 오름차순, 5번째 선수의 등수
  # 점수가 가장 낮은 팀이 우승, 점수가 같다면 5번째 선수가 먼저 들어온 경우 우승
  new_data.sort(key=lambda x:(sum(x[1:5]), x[5]))
  # 랭킹 반환
  return new_data[0][0]

def solution(N, data):
  # 6명인지 확인
  six_team_rank = check_six(data)
  # 우승팀 확인
  res = check_score(six_team_rank)
  return res # 우승 팀의 번호 반환

def main():
  # 테스트 케이스
  T = int(input())
  for _ in range(T):
    # 순위의 개수
    N = int(input())
    # 선수가 들어온 순서
    data = list(map(int,input().split()))
    # 우승팀의 번호 출력
    print(solution(N, data))

if __name__ == "__main__":
  main()