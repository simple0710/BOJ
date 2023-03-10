# 2023/03/10 Greedy
# https://www.acmicpc.net/problem/2831
import sys
input = sys.stdin.readline

def search(p_arr, m_arr):
  global res
  for p in p_arr:
    while m_arr:
      check = m_arr.pop(0)
      if p < check: # 쌍을 이룰 수 있는 경우
        res += 1
        break

N = int(input())
p_man = sorted(list(map(int,input().split())))
p_woman = sorted(list(map(int,input().split())))
m_man = []
m_woman = []
# 양수 배열과 음수 배열 분류 및 정렬
while p_man and p_man[0] < 0:
  m_man.append(-p_man.pop(0))
while p_woman and p_woman[0] < 0:
  m_woman.append(-p_woman.pop(0))
m_man.sort()
m_woman.sort()

res = 0
# 탐색 시작
search(p_man, m_woman)
search(p_woman, m_man)

# 정답 출력
print(res)