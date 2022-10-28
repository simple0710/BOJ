# 2022/10/28

# 정보 입력
A, P = map(int,input().split())
arr = [A]
while True:
  sum = 0
  for i in str(arr[-1]):
    sum += int(i) ** P
  # 반복이 시작됐을 경우
  if sum in arr:
    break
  arr.append(sum)

# 출력  
print(arr.index(sum))