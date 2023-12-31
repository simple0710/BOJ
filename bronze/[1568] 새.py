# 2023/12/31 Implementation, Math
# https://www.acmicpc.net/problem/1568
def main():
  N = int(input())
  cnt = 1
  res = 0
  while N > 0:
    # N이 지금 불러야 하는 수보다 작다면 1부터 다시 시작한다.
    if N < cnt: cnt = 1
    N -= cnt
    cnt += 1
    res += 1
  print(res) # 모든 새가 날아가는데 걸리는 시간 출력한다.

if __name__ == "__main__":
  main()