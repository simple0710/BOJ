# 2023/01/28 두 포인터, 슬라이딩 윈도우
# https://www.acmicpc.net/problem/15961
import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
# 초밥 정보 입력
cho_list = [int(input()) for _ in range(N)]
cho_list.extend(cho_list) # 원형 벨트 이므로 하나 더 추가

cnt_dict = defaultdict(int) # 초밥 종류 개수 딕셔너리
cnt_dict[c] += 1 # 기본적으로 추가
left = 0
right = 0

# 일단 k개 만큼 추가한다.
while right < k:
  cnt_dict[cho_list[right]] += 1
  right += 1

# 탐색 시작
res = 0
while right < len(cho_list):
  res = max(res, len(cnt_dict))

  # 왼쪽 값은 빼고 오른쪽 값은 더한다.
  cnt_dict[cho_list[left]] -= 1
  if cnt_dict[cho_list[left]] == 0: # 초밥을 먹지 않은 경우 제거
    del cnt_dict[cho_list[left]]
  cnt_dict[cho_list[right]] += 1
  
  # 한칸씩 오른쪽으로 이동
  left += 1
  right += 1

# 정답 출력
print(res)