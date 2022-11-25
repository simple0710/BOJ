# 2022/11/25 에라토스테네스의 체, 소수 판정
# 에라토스테네스의 체를 이용해 소수와 소수가 아닌 리스트 반환
def prime_list(n):
  v = [True] * n
  for i in range(2, int(n**0.5) + 1):
    # 소수인 경우
    if v[i] == True:
      # 해당 소수의 배수를 False로 한다.
      for j in range(i+i, n, i):
        v[j] = False
  # 리스트 반환
  return v

data = prime_list(1000000)
while True:
  # 입력
  N = int(input())
  # 0인 경우 종료
  if N == 0:
    break
  # 절반을 넘으면 반복이기 때문에 N//2까지만 수행
  for i in range(3, N//2 + 1):
    # 양 쪽다 소수인 경우 출력 후 종료
    if data[i] and data[N-i]:
      print(f'{N} = {i} + {N - i}')
      break