# 2023/11/29 Implementation, Math
# https://www.acmicpc.net/problem/13300
def main():
  # 학생 수, 최대 인원 수
  N, K = map(int,input().split())
  room = [[0] * 7 for _ in range(2)]
  for _ in range(N):
    # 성별, 학년
    S, Y = map(int,input().split())
    room[S][Y] += 1
  res = 0
  for i in room:
    for j in i:
      res += j // K
      if j % K: # 남는 사람이 있는 경우 방을 하나 더 추가한다.
        res += 1
  print(res) # 최소 방의 개수 출력

if __name__ == "__main__":
  main()