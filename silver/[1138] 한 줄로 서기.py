n = int(input())
data = list(map(int,input().split()))
arr = [i for i in range(1,n+1)]

for i in range(n-1,-1,-1):
  j = arr.index(i+1)
  # data[i]가 0 이상인 경우 실행한다.
  while data[i] > 0:
    # 만약 오른쪽 수가 크다면 data[i] -= 1을 수행한다.
    if arr[j] < arr[j+1]:
      data[i] -= 1
    # 위치를 바꾸고 해당 인덱스를 +1 한다.
    arr[j], arr[j+1] = arr[j+1], arr[j]
    j += 1
print(' '.join(map(str,arr)))
