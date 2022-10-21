# 근의 제곱 사용 n(n+1)/2 <= length/2 ## n은 중간까지의 거리
# -b +-(sqrt(b**2-4ac)) => n**2 + n -length
# 중간 까지 가는데는 속도가 올라가고 그 다음부터는 속도가 내려간다.

for _ in range(int(input())):
  x, y = map(int,input().split())
  length = y - x
  # **(1/2)는 루트
  # 근의 공식을 이용해 lenght/2보다 작은 정수합의 최대 정수를 구한다.
  n = int(((-1) + (1+4 * length)**(1/2))/2)

  # 두 번 이동하고 남은 거리 측정
  remainder = length - n * (n + 1)
  # 작동횟수 추가
  operations = 2 * n

  # 2*n를 이동하고 거리가 남았을 경우
  if 0 < remainder <= n + 1:
    operations += 1
  # 작동 횟수 추가
  elif remainder > n + 1:
    operations += 2

  print(operations)