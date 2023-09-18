# 2023/08/20 Implementation, String
# https://www.acmicpc.net/problem/28691
import sys
input = sys.stdin.readline

def solution(s):
    data = {'M':"MatKor", 'W':"WiCys", "C":"CyKor", "A":"AlKor", "$":"$clear"}
    # 주어진 문자에 따른 동아리의 전체 이름 출력
    print(data[s])

def main():
  s = input().rstrip()
  solution(s)

if __name__ == "__main__":
  main()