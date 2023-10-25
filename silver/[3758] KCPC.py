# 2023/10/25 Implementation, Sorting
# https://www.acmicpc.net/problem/3758
import sys
input = sys.stdin.readline

# Solution 1
# 주어진 조건에 맞게 순위를 정렬한다.
def solution1():
  # 팀의 개수, 문제의 개수, 나의 팀 ID, 로그 엔트리의 개수
  n, k, t, m = map(int,input().split())
  score = [[0] * (k + 1) for _ in range(n+1)]
  submit = [0] * (n + 1)
  last_submit = [0] * (n + 1)
  for idx in range(m):
    # 팀 ID, 문제 번호, 획득한 점수
    i, j, s = map(int,input().split())
    score[i][j] = max(score[i][j], s)
    submit[i] += 1
    last_submit[i] = idx

  res = 1
  my_score = sum(score[t][1:])
  for i in range(1, n+1):
    if i == t: # 같은 경우는 제외
      continue
    # 내 팀의 점수가 상대 팀보다 낮은 경우
    if my_score < sum(score[i][1:]):
      res += 1
    elif my_score == sum(score[i][1:]):
      # 내 팀의 제출 횟수가 상대 팀보다 큰 경우
      if submit[t] > submit[i]: 
        res += 1
      elif submit[t] == submit[i]:
        # 내 팀의 마지막 제출 시간이 상대 팀보다 느린 경우
        if last_submit[t] > last_submit[i]:
          res += 1
  return res # 내 팀의 순위 반환

# Solution 2
# Solution 1을 간략하게 정렬하는 방법
def solution2():
  # 팀의 개수, 문제의 개수, 나의 팀 ID, 로그 엔트리의 개수
  n, k, t, m = map(int,input().split())
  score = [[0] * (k+3) + [i] for i in range(n+1)]
  for idx in range(m):
    # 팀 ID, 문제 번호, 획득한 점수
    i, j, s = map(int,input().split())
    score[i][j] = max(score[i][j], s)
    score[i][k+1] += 1 # 제출 횟수
    score[i][k+2] = idx # 마지막 제출
  score = score[1:]
  # 마지막 제출, 제출 횟수, 점수를 정렬한다.
  # 점수는 내림차순으로 정렬한다.
  score.sort(key=lambda x:(-sum(x[:k+1]), x[k+1], x[k+2]))
  for i in range(n):
    if score[i][k+3] == t: # 내 팀의 ID인 경우 순위 반환
      return i + 1

def main():
  T = int(input())
  for _ in range(T):
    # print(solution())
    continue

if __name__ == "__main__":
  main()