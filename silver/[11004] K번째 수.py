# 2024/01/02 Sorting
# https://www.acmicpc.net/problem/11004
def main():
  N, K = map(int,input().split())
  # 배열을 정렬한다.
  arr = sorted(list(map(int, input().split())))
  print(arr[K-1]) # K번째 수를 출력한다.

if __name__ == "__main__":
  main()