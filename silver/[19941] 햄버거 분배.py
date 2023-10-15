# 2023/10/16 Greedy
# https://www.acmicpc.net/problem/19941
import sys, heapq
input = sys.stdin.readline

'''
# Solution 1
우선순위큐로 햄버거와 사람의 위치를 구한 뒤,
해당 인덱스로 먹을 수 있는지 확인한다.
'''
def solution1(N, K, place):
  res = 0
  hamburger = []
  people = []
  # 사람이 있는 위치와 행범거가 있는 위치를 저장
  for i in range(N):
    heapq.heappush(hamburger if place[i] == 'H' else people, i)

  # 사람과 햄버거의 위치를 비교한다.
  while people: # 사람이 아직 있는 경우
    pv = heapq.heappop(people)
    while hamburger: # 햄버거가 있는 경우
      hv = heapq.heappop(hamburger)
      if hv - pv > K: # 범위 내에 햄버거가 없는 경우 다음 사람을 확인
        heapq.heappush(hamburger, hv) # 범위 밖의 값을 반환했으니 다시 추가
        break
      elif abs(pv - hv) <= K: # 범위 내에 햄버거가 있는 경우 정답 갱신
        res += 1
        break
  return res # 햄버거를 먹을 수 있는 사람의 수 반환

'''
# Solution 2
사람이 있는 위치에서 K거리만큼 확인하고,
햄버거인 경우 정답을 갱신한다.
'''
def solution2(N, K, place):
  res = 0
  place = list(place)
  for i in range(N):
    if place[i] == 'P': # 사람인 경우
      # K거리만큼 확인
      for j in range(max(i-K, 0), min(i+K+1, N)):
        if place[j] == 'H': # 햄버거인 경우
          # 먹은 처리 및 정답 갱신 후 종료
          place[j] = ''
          res += 1
          break
  return res # 햄버거를 먹을 수 있는 사람의 수 반환

def main():
  # 식탁의 길이, 햄버거를 선택할 수 있는 거리
  N, K = map(int,input().split())
  # 사람과 햄버거의 위치
  place = input().rstrip()
  # print(solution(N, K, place)) # 햄버거를 먹을 수 있는 사람의 수 출력

if __name__ == "__main__":
  main()