# 2023/10/13 Bruteforcing, SlidingWindow
# https://www.acmicpc.net/problem/1522
import sys
input = sys.stdin.readline

# Solution1
# 각각의 a, b에 대해서 SlidingWindow 시행 후, 교환해야하는 횟수를 구한다.
def find(s, v, c):
  cnt = len(s)
  # 맨 처음 a와 b의 개수 저장
  cnt_dict = {'a' : s[:c].count('a'), 'b' : s[:c].count('b')}
  p = c # 점
  ns = s + s[:c] # 원형이므로 탐색범위만큼 추가한다.
  while p < len(ns):
    cnt = min(cnt, cnt_dict[v]) # 정답 갱신
    cnt_dict[ns[p-c]] -= 1 # 지난 위치의 문자 개수 감소
    cnt_dict[ns[p]] += 1 # 만난 위치의 문자 개수 증가
    p += 1 # 범위 이동
  return cnt # 최소 교환 횟수 반환

def solution1(s):
  a_cnt = s.count('a')
  b_cnt = s.count('b')
  # a와 b에 대해서 SlidingWindow 수행 후, 최솟값을 구한다.
  res = min(find(s, 'b', a_cnt), find(s, 'a', b_cnt))
  return res # 최소 교환 횟수 반환

# Solution2
# 한 문자에 대해 SlidingWindow 시행 후, 교환해야하는 횟수를 구한다.
def solution2(s):
  res = len(s)
  a_cnt = s.count('a') # 탐색 범위
  bs_cnt = s[:a_cnt].count('b') # 현재 교환해야 하는 횟수
  p = a_cnt # 점
  ns = s + s[:a_cnt] # 원형이므로 탐색범위만큼 추가한다.
  while p < len(ns):
    res = min(res, bs_cnt) # 정답 갱신
    if ns[p-a_cnt] == 'b': # 교환해야하는 수를 지난 경우
      bs_cnt -= 1
    if ns[p] == 'b': # 교환해야하는 수를 만난 경우
      bs_cnt += 1
    p += 1 # 범위 이동
  return res # 최소 교환 횟수 반환

def main():
  # a와 b로만 이루어진 문자열 입력
  string = input().rstrip()
  # print(solution(string)) # 코드 실행 후 교환 횟수 출력

if __name__ == "__main__":
  main()