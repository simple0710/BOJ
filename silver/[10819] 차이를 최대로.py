# 2022/11/24 백트래킹
def back():
  global res
  # 해당 길이가 된 경우
  if len(s) == N:
    check = 0
    # 주어진 계산식을 수행
    for i in range(N-1):
      check += abs(s[i][1] - s[i + 1][1])
    # 결과가 더 큰 쪽을 정답으로 정한다.
    res = max(res, check)
    return
  # 전 지역 탐색
  for i in range(N):
    # 중복의 경우가 있기 때문에 인덱스와 값을 저장한다.
    if (i, arr[i]) not in s:
      s.append((i, arr[i]))
      back()
      s.pop()

# 정보 입력
N = int(input())
arr = list(map(int,input().split()))
s = []
res = 0
# 백트래킹 시작
back()
# 정답 출력
print(res)