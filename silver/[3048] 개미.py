# 2023/11/11 String, Implementation, Simulation
# https://www.acmicpc.net/problem/3048
import sys
input = sys.stdin.readline

def solution(idx_group, N1, N2):
  i = 0
  while i < N1 + N2 - 1:
    # 오른쪽 방향과 왼쪽 방향이 마주친 경우
    if idx_group[i] < N1 and idx_group[i+1] >= N1:
      # 위치 변경
      idx_group[i], idx_group[i+1] = idx_group[i+1], idx_group[i]
      i+=1 # 다음 케이스는 넘긴다.
    i+=1 # 다음 인덱스 확인

def main():
  # 각 그룹의 수
  N1, N2 = map(int,input().split())
  # 왼쪽에서 오른쪽으로 가는 그룹
  group1 = input().rstrip()[::-1]
  # 오른쪽에서 왼쪽으로 가는 그룹
  group2 = input().rstrip()
  # 최초 위치 인덱스
  idx_group = [i for i in range(N1+N2)]
  T = int(input())
  # T 초간 탐색
  for _ in range(T):
    # 위치 변경
    solution(idx_group, N1, N2)
  # 정답 확인용 그룹
  res_check_group = list(group1 + group2)
  # 최종 위치 출력
  print(''.join([res_check_group[i] for i in idx_group]))

if __name__ == "__main__":
  main()