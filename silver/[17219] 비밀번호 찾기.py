# 2023/08/19 Datastructures, Hash-Set
# https://www.acmicpc.net/problem/17219
import sys
input = sys.stdin.readline

def solution(M, data):
  for _ in range(M): # 원하는 사이트의 비밀번호 출력
    site = input().rstrip()
    print(data[site])

def main():
  N, M = map(int,input().split())
  data = {}
  for _ in range(N): # 사이트 비밀번호 저장
    site, password = input().rstrip().split()
    data[site] = password
  solution(M, data) # 탐색 시작

if __name__ == "__main__":
  main()