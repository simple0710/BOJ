import math

# 소수 여부를 확인한다.
def isPrime(x):
  if x == 1:
    return False
  for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
      return False
  return True
  
n = int(input())
result = 0
while True:
  # 펠린드롬 수이고, 소수인 경우 result를 저장하고 종료
  if str(n) == str(n)[::-1]:
    if isPrime(n):
      result = n
      break
  n += 1
  
# 출력
print(result)