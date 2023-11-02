# 2023/11/02 Implementation, Bruteforcing, Bactracking
# https://www.acmicpc.net/problem/22251
import sys
input = sys.stdin.readline

LED_light = {
  '0': [1, 0, 1, 1, 1, 1, 1],
  '1': [0, 0, 0, 0, 1, 0, 1],
  '2': [1, 1, 1, 0, 1, 1, 0],
  '3': [1, 1, 1, 0, 1, 0, 1],
  '4': [0, 1, 0, 1, 1, 0, 1],
  '5': [1, 1, 1, 1, 0, 0, 1],
  '6': [1, 1, 1, 1, 0, 1, 1],
  '7': [1, 0, 0, 0, 1, 0, 1],
  '8': [1, 1, 1, 1, 1, 1, 1],
  '9': [1, 1, 1, 1, 1, 0, 1],
}

# 상중하, 좌우, 좌우
def back(idx, total):
  global s

  if idx == int(K): # 탐색 끝
    num = int(''.join(map(str, X)))
    if 0 < num <= int(N): # 층 범위 안인 경우 정답 리스트에 추가
      s.add(tuple(X))
    return

  for i in range(idx, int(K)):
    for j in range(10): # 0 부터 9 까지 비교
      cnt = 0
      for k in range(7): # 반전 확인
        # 반전 횟수 추가
        cnt += LED_light[str(X[i])][k] != LED_light[str(j)][k]
      if total + cnt <= int(P): # 총 반전 횟수가 P보다 작은 경우
        before = X[i]
        X[i] = j
        back(i + 1, total + cnt) # 다음 확인
        X[i] = before

def solution():
  global s
  s = set()
  back(0, 0) # 탐색 시작
  # 반전시킬 수 있는 경우의 수 출력
  # X층은 제외한다.
  print(len(s)-1)

def main():
  global N, K, P, X
  # N층, K자리, 1개 ~ P개 반전, 현재 X층
  # 9 1 2 5 -> 3 6 8 9
  N, K, P, X = input().rstrip().split()
  X =  [0] * (len(N) - len(X)) + list(map(int, X))
  solution()

if __name__ == "__main__":
  main()