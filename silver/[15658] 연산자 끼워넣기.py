# 2022/11/28 백트래킹
# 백트래킹
def back(depth, check):
  global max_res, min_res

  # 길이가 일정 길이에 도달한 경우
  if depth == N:
    max_res = max(max_res, check)
    min_res = min(min_res, check)
    return
  # 각 연산의 남은 횟수가 있는 경우 수행
  if s[0] > 0:
    s[0] -= 1
    back(depth+1, check + arr[depth])
    s[0] += 1
  if s[1] > 0:
    s[1] -= 1
    back(depth+1, check - arr[depth])
    s[1] += 1
  if s[2] > 0:
    s[2] -= 1
    back(depth+1, check * arr[depth])
    s[2] += 1
  if s[3] > 0:
    s[3] -= 1
    back(depth+1, int(check / arr[depth]))
    s[3] += 1

# 정보 입력
N = int(input())
arr = list(map(int,input().split()))
s = list(map(int,input().split()))
max_res = -int(1e10)
min_res = int(1e10)

# 백트래킹 시작
back(1, arr[0])

# 정답 출력
print(max_res)
print(min_res)