# 2023/11/19 Implementation
# https://www.acmicpc.net/problem/2621
from collections import defaultdict
import sys
input = sys.stdin.readline

'''
5장 같은 색
4장 같은 숫자
3장 숫자, 2장 숫자 같을 때 * 10 + 2장 + 700 
5장 카드 색갈이 같을 때 600
5장 카드 연속될 때 500
5장 중 3장 숫자 같을 때 400
5장중 2장 숫자, 2중 숫자
2장 숫자
나머지
'''

def solution(cards):
  color_dict = defaultdict(int)
  number_dict = defaultdict(int)
  # 카드 확인
  for color, number in cards:
    color_dict[color] += 1
    number_dict[int(number)] += 1

  score = 0
  same_color = False
  same_number = False
  # 4. 같은 색상 확인
  if len(color_dict) == 1:
    score = max(score, max(number_dict) + 600)
    same_color = True
  # 5. 연속적인 숫자인 경우
  if len(number_dict) == 5 and max(number_dict) - min(number_dict) == 4:
    score = max(score, max(number_dict) + 500)
    same_number = True
  # 1. 모두 같은 색, 연속적인 숫자
  if same_color and same_number:
    score = max(score, max(number_dict) + 900)

  for number, cnt in number_dict.items():
    # 2. 4장의 숫자가 같은 경우
    if cnt == 4:
      score = max(score, number + 800)
    # 6. 3장의 숫자가 같은 경우
    elif cnt == 3:
      score = max(score, number + 400)
      # 3. 나머지 2장도 숫자가 같은 경우
      if len(number_dict) == 2:
        two = [i for i in number_dict if i != number][0]
        score = max(score, number * 10 + two + 700)
    # 8. 2장의 숫자가 같은 경우
    elif cnt == 2:
      score = max(score, number + 200)
      v = len(number_dict) - 1
      # 7. 다른 2장의 숫자가 같은 경우
      if v == 2:
        s = [i for i in number_dict if i != number and number_dict[i] == 2][0]
        score = max(score, max(number, s) * 10 + min(number, s) + 300)
  # 9. 어떤 경우도 해당하지 않는 경우
  score = max(score, max(number_dict) + 100)
  return score # 최대 점수 반환

def main():
  # 카드 색과 숫자 데이터
  cards = [input().rstrip().split() for _ in range(5)]
  print(solution(cards)) # 최대 점수 출력

if __name__ == "__main__":
  main()