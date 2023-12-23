# 2023/12/23 Math, Implementation
# https://www.acmicpc.net/problem/2875
def main():
  N, M, K = map(int,input().split())
  res = 0
  # 여자와 남자의 수를 각각 뺀 모든 경우를 확인한다.
  for i in range(K+1): res = max(res, min((N-i)//2, M-(K-i)))
  print(res) # 만들 수 있는 팀의 최대 개수 출력

if __name__ == "__main__":
  main()