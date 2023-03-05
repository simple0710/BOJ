# 2023/03/05 구현
# https://www.acmicpc.net/problem/5073
while True:
  n = sorted(list(map(int,input().split())))
  if sum(n) == 0: # 0만 입력받은 경우
    break
  elif n[2] >= n[0] + n[1]: # 가장 긴 변이 나머지의 합보다 크거나 같은 경우
    print("Invalid")
  elif n[0] == n[1] == n[2]: # 세 변의 길이가 같은 경우
    print("Equilateral")
  elif (n[0] == n[1]) or (n[1] == n[2]) or (n[0] == n[2]): # 두 변의 길이가 같은 경우
    print("Isosceles")
  else: # 세 변의 길이가 다른 경우
    print("Scalene")
