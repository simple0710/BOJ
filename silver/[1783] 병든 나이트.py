# 2023/12/22 Greedy
# https://www.acmicpc.net/problem/1783
def solution(N, M):
  # 맨 처음 위치에만 있을 수 있다.
  if N == 1:
    return 1
  # 4를 넘으면 방법에 대한 조건이 생기므로 4를 초과할 수 없다.
  elif N == 2:
    return min(4, (M+1)//2)
  # M이 4보다 작다거나 같면 방문 횟수는 M이 된다.
  elif M <= 6:
    return (min(4, M))
  # M이 6보다 큰 경우 방문 횟수는 M-2가 된다.
  else:
    return M-2
    
def main():
  N, M = map(int,input().split())
  print(solution(N, M)) # 방문할 수 있는 칸의 최대 개수 출력

if __name__ == "__main__":
  main()