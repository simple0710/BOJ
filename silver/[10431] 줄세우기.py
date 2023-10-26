# 2023/10/26 Implementation, Simulation
# https://www.acmicpc.net/problem/10431
import sys
input = sys.stdin.readline

def solution(data):
  people = data[1:]
  res = 0
  for i in range(len(people)):
    # 모든 값과 비교
    for j in range(i+1, len(people)):
      # i가 j보다 더 큰 경우, 위치 변경
      if people[i] > people[j]:
        people[i], people[j] = people[j], people[i]
        res += 1
  # 테스트 케이스의 번호, 학생들이 뒤로 물러난 걸음 수의 총합 반환 
  return (data[0], res)

def main():
  P = int(input()) # 테스트 케이스
  for _ in range(P):
    # 테스트 케이스의 번호, 아이들의 키
    data = list(map(int,input().split()))
    # 테스트 케이스의 번호, 학생들이 뒤로 물러난 걸음 수의 총합 출력
    print(*solution(data))

if __name__ == "__main__":
  main()