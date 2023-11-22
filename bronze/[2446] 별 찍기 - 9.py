# 2023/11/22 Implementation
# https://www.acmicpc.net/problem/2446
def main():
  N = int(input())
  # 위쪽 별 찍기
  for i in range(N):
    print(' ' * i + '*' * (2 * (N - i) - 1))
  # 아래쪽 별 찍기
  for i in range(1, N):
    print(' ' * (N - i - 1) + '*' * (2 * i + 1))
if __name__ == "__main__":
  main()