# 2023/10/30 DataStructures, String, Sorting, Hash-Set
# https://www.acmicpc.net/problem/20920
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(N, M, words):
  word_cnt_dict = defaultdict(int)
  # 단어가 나온 빈도수를 확인
  for word in words: word_cnt_dict[word] += 1
  # 길이가 M 이상인 단어 저장
  word_check_list = list([(word, word_cnt_dict[word]) for word in word_cnt_dict if len(word) >= M])
  # 우선 순위로 정렬
  word_check_list.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))
  # 단어장 반환
  return [word[0] for word in word_check_list]

def main():
  # 단어의 개수, 외울 단어의 길이 기준
  N, M = map(int,input().split())
  # 외울 단어
  words = [input().rstrip() for _ in range(N)]
  res = solution(N, M, words) # 단어 확인
  # 단어장 출력
  for word in res:
    print(word)

if __name__ == "__main__":
  main()