# 2023/08/21 Greedy, Sorting
# https://www.acmicpc.net/problem/28464
import sys
input = sys.stdin.readline

def solution(N, data):
  res1 = 0 # 가장 적게 가져가기
  res2 = 0 # 가장 많이 가져가기
  data.sort()
  for i in range(N // 2): # 절반까지 서로 같은 양만큼 접시를 고른다.
    res1 += data[i]
    res2 += data[-i - 1]
  if N % 2 == 1: # 접시가 하나 남은 경우 박 모 씨가 접시를 가져간다.
    res2 += data[N//2]
  print(res1, res2) # 각각 가져간 감자튀김의 양을 출력한다.

def main():
  N = int(input())
  data = list(map(int,input().split()))
  solution(N, data) # 코드 실행

if __name__ == "__main__":
  main()