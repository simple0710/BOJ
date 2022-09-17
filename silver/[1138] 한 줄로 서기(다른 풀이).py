n = int(input())
data = list(map(int,input().split()))
arr = [0] * n

for i in range(n):
  cnt_zero = 0
  for j in range(n):
    # 만약 cnt_zero가 h[i]와 같고, result[j] 자리가 빈 자리인 경우 값을 삽입한다.
    if cnt_zero == data[i] and arr[j] == 0:
      arr[j] = i + 1
      break
    # 빈자리인 경우 cnt_zero += 1을 실행한다
    elif arr[j] == 0:
      cnt_zero += 1
print(' '.join(map(str, arr)))