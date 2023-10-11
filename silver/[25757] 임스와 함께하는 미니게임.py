# 2023/10/11 DataStructures, String, Hash-Set
# https://www.acmicpc.net/problem/25757
import sys
input = sys.stdin.readline

def solution(N, G, P):
   # 임스는 중복된 사람과 게임을 다시 플레이 하지 않는다.
   # 따라서 중복되지 않은 사람 // 게임의 플레이어 수가 성립한다.
  tp = {'Y' : 1, 'F' : 2, 'O' : 3}
  return len(set(P)) // tp[G] # 정답 반환

def main():
  N, G = input().rstrip().split()
  participant = [input().rstrip() for _ in range(int(N))]
  print(solution(N, G, participant)) # 최대 게임 플레이 수 출력

if __name__ == "__main__":
  main()