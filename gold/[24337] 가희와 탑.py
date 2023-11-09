# 2023/11/09 Greedy, Constructive
# https://www.acmicpc.net/problem/24337
import sys
input = sys.stdin.readline

def solution(N, A, B):
  # 기초 건물 높이
  left = [i for i in range(1, A+1)]
  right = [i for i in range(1, B+1)]
  # 대체할 수 있는 높이를 제거한다.
  # left = [1, 2, 3]이고, right = [1, 2, 3]일 때, 높이 3의 건물은 하나만 있어도 된다.
  if left[-1] < right[-1]:
    left.pop()
  else:
    right.pop()

  # 건물들의 높이 정보가 존재하지 않는 경우
  # N개 넘게 있어야 정보가 존재하는 경우
  if len(right + left) > N:
    return -1

  # 부족한 길이 채우기
  tower = left + right[::-1]
  if A >= B:
    tower = [1] * (N - len(tower)) + tower
  else:
    tower = [tower[0]] + [1] * (N - len(tower)) + tower[1:]
  # 건물들의 높이 정보 반환
  return ' '.join(map(str, tower))

def main():
  # N : 건물의 개수
  # A : 가희가 볼 수 있는 건물의 개수
  # B : 단비가 볼 수 있는 건물의 개수
  N, A, B = map(int,input().split())
  # 건물들의 높이 정보 출력
  print(solution(N, A, B))

if __name__ == "__main__":
    main()