# 2023/07/25 BFS
# https://www.acmicpc.net/problem/14496
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque([A])
  visited = [-1] * (N + 1)
  visited[A] = 0
  while q:
    now_word = q.popleft()
    if now_word == B: # 목표 문자로 치환한 경우
      return visited[now_word]
    for change_word in word_change_list[now_word]: # 치환 가능 리스트 확인
      if visited[change_word] == -1: # 아직 치환을 해본 적이 없는 경우 
        q.append(change_word)
        visited[change_word] = visited[now_word] + 1
  return -1 # 불가능한 경우
A, B = map(int,input().split())
N, M = map(int,input().split())
word_change_list = [[] for _ in range((N + 1))]
for _ in range(M):
  word1, word2 = map(int,input().split())
  word_change_list[word1].append(word2)
  word_change_list[word2].append(word1)
print(bfs()) # 탐색 및 정답 출력