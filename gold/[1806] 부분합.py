# 2022/11/08 두 포인터, 누적 합
MAX = int(1e9)

# 두 포인터
def pointer(start, end):
  sum = 0
  ans = MAX
  while True:
    # 구하려는 값보다 sum이 크다면 
    # 1. ans와 비교해 최소 길이를 저장한다.
    # 2. start + 1을 하고 이전 data[start] 값을 뺀다.
    if sum >= S:
      ans = min(ans, end - start)
      sum -= data[start]
      start += 1
    # N에 도달한 경우 ans를 반환하고 종료
    elif end == N:
      return ans
    # 구하려는 값보다 sum이 작다면
    # data[end] 값을 sum에 더하고 end + 1을 수행한다.
    else:
      sum += data[end]
      end += 1

if __name__ == "__main__":
  # 정보 입력
  N, S = map(int,input().split())
  data = list(map(int,input().split()))

  # 탐색 시작
  ans = pointer(0, 0)
  # 값이 변하지 않았다면 0 출력
  if ans == MAX:
    print(0)
  # 값을 구했다면 ans 출력
  else:
    print(ans)
