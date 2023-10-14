# 2023/09/17 Implementation
# https://www.acmicpc.net/problem/30035
import sys, math
input = sys.stdin.readline

def solution():
  total = N
  liar_flag = False
  now_rank = 0
  min_, max_ = -1, -1
  for info in data:
    if info[1][-1] != '%': # 고정 티어
      people = min(total, int(info[1]))
    else: # 상대 티어
      info[1] = int(info[1][:-1])
      # 내림차로 한다.
      people = int(math.floor(total * info[1] / 100))

    if info[0] == friends: # 친구의 티어명과 같은 경우
      if people < tier: # 부른 티어가 있을 수 없는 경우 'Liar'
        liar_flag = True
    if people: # 사람이 있는 경우 (0명인 경우도 주어진다.)
      now_rank = N - total + 1
      my_tier_list = [now_rank]
      cnt = 0
      # 최대한 인원을 분배한다.
      for _ in range(1, min(people, 4)+1):
        my_tier_list.append(math.ceil(people/min(people, 4)))
        cnt += math.ceil(people/min(people, 4))
      idx = 1
      if abs(cnt-people): # 초과되는 수가 있는 경우
        over = abs(cnt-people)
        # 초과된 분만큼 순위를 줄인다.
        # 이때, 하나의 순위만 줄이는 것이 아닌, 
        # 모든 순위가 최소 1을 유지할 수 있을 만큼만 줄인다.
        while over:
          if my_tier_list[-idx] - over > 0:
            my_tier_list[-idx] -= over
            over = 0
          else:
            over -= my_tier_list[-idx] - 1
            my_tier_list[-idx] -= my_tier_list[-idx] - 1
          idx += 1

      if info[0] == friends: # 구하고자 하는 티어인 경우
        if tier == -1: # 티어가 불리지 않은 경우
          # 가장 낮은 순위와 가장 높은 순위를 값으로 가진다.
          min_ = my_tier_list[0]
          max_ = my_tier_list[0] + sum(my_tier_list[1:]) - 1
        else: # 티어가 불린 경우
          # 해당 티어의 가장 낮은 순위와 가장 높은 순위를 값으로 가진다.
          min_ = sum(my_tier_list[:tier])
          max_ = sum(my_tier_list[:tier+1])-1
      # 구한 유저 수 빼기
      total -= people
      
  if total: # 모든 유저의 티어를 정할 수 없는 경우
    print('Invalid System')
  elif liar_flag or (min_, max_) == (-1, -1): # 티어가 올바르지 않거나, 해당 티어가 없는 경우
    print("Liar")
  else: # 그 외의 경우
    print(min_, max_)

def main():
  global N, T, data, friends, tier
  N, T = map(int,input().split())
  data = [list(input().rstrip().split()) for _ in range(T)]
  friends = input().rstrip()
  tier = -1
  if friends[-1].isdecimal(): # 티어가 있는 경우 티어 저장
    tier = int(friends[-1])
    friends = friends[:-1]
  solution() # 탐색 시작

if __name__ == "__main__":
  main()