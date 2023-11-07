# 2023/11/07 DataStructures, String, Sorting, Hash-Set
# https://www.acmicpc.net/problem/2179
from collections import defaultdict
import sys
input = sys.stdin.readline
# 두 단어의 접두사의 길이로 측정한다.
# 접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다.

def solution(word_list):
  cnt_dict = defaultdict(int)
  # 모든 영단어의 부분문자열 개수 확인
  for word in word_list:
    for i in range(1, len(word)+1):
      cnt_dict[word[:i]] += 1

  # 부분문자열이 2개 이상 있는 영단어만 저장
  check = [(i, cnt_dict[i]) for i in cnt_dict if cnt_dict[i] > 1]
  # 부분문자열 내림차순 정렬
  check.sort(key = lambda x : -len(x[0]))

  # 정답 출력
  cnt = 0
  same_word = check[0][0]
  for word in word_list:
    if len(word) >= len(same_word):
      # 부분문자열이 같은 경우
      if word[:len(same_word)] == same_word:
        print(word)
        cnt += 1
        if cnt == 2: # 가장 앞에 있는 두 문자열을 출력하고 종료
          break

def main():
  # 영단어 수
  N = int(input())
  # 서로 다른 영단어 목록
  word_list = [input().rstrip() for _ in range(N)]
  # 코드 실행
  solution(word_list)

if __name__ == "__main__":
  main()