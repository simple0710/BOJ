# 2023/10/21 String, Parsing, DataStructures, Hash-Set
# https://www.acmicpc.net/problem/22233
import sys
input = sys.stdin.readline

def solution(memo_keyword, blog_keyword):
  memo_keyword = set(memo_keyword) # 집합으로 변환
  for keywords in blog_keyword: # 블로그에서 M 번째 글을 가져온다.
    for word in keywords: # M 번째 글에 있는 키워드를 가져온다.
      memo_keyword.discard(word) # 메모장에 있는 키워드를 지운다.
    print(len(memo_keyword)) # 메모장에 남은 키워드 출력

def main():
  # 메모장에 적은 키워드 개수, 블로그에 쓴 글 수
  N, M = map(int,input().split())
  # 메모장
  memo_keyword = [input().rstrip() for _ in range(N)]
  # 블로그(','로 구분됨)
  blog_keyword = [input().rstrip().split(',') for _ in range(M)]
  solution(memo_keyword, blog_keyword) # 코드 실행

if __name__ == "__main__":
  main()