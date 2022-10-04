# 이분 탐색으로 k 찾기
def binary():
  start, end = 1, n

  if search(n) < k:
    return -1

  while start <= end:
    mid = (start + end) // 2
    
    # 1부터 mid까지의 자릿수
    n_mid = search(mid)

    if n_mid < k:
      start = mid + 1
    else:
      end = mid - 1
      answer = mid

  return answer

# 길이 구하기
def search(num):  
  length = len(str(num))
  result = 0 

  for i in range(1, length):
    result += i * (pow(10, i) - pow(10, i-1)) 
  result += length * (num - pow(10,length-1) + 1)

  return result

#####
n, k = map(int,input().split())

answer = binary()

if answer == -1:
  print(-1)
else:
  ind = search(answer) - k + 1
  answer = str(answer)
  print(int(answer[-ind]))