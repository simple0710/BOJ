# 2023/08/18 Greedy, String, Sorting
# https://www.acmicpc.net/problem/29198
import sys
input = sys.stdin.readline

def solution(data, M, K):
  data.sort() # 데이터 정렬
  # K까지 문자열 추가
  res = ''
  for i in data[:K]:
    res += ''.join(map(str, i))
  # 저장되어진 문자열을 정렬한 것이 정답이 된다.
  res = ''.join(map(str, sorted(res)))
  return res # 문자열 반환
def main():
  N, M, K = map(int,input().split())
  data = []
  for _ in range(N):
    data.append(sorted(input().rstrip()))
  print(solution(data, M, K)) # 정답 출력

if __name__ == "__main__":
  main()