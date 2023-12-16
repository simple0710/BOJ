# 2023/12/17 Implementation, Combinatorics, Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/16922
def main():
  N = int(input())
  number = set([1, 5, 10, 50])
  for _ in range(1, N):
    new_number = set()
    # 이전의 수를 확인한다.
    for k in list(number):
      # 이전의 수와 현재 칸에 넣을 수 있는 수의 합을 집합에 추가한다. 
      for j in [1, 5, 10, 50]: new_number.add(k+j)
    # 집합 갱신
    number = new_number
  # # N개를 사용해서 만들 수 있는 서로 다른 수의 개수 출력
  print(len(number))

if __name__ == "__main__":
  main()