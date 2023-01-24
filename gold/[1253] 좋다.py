# 2023/01/23 두 포인터
# https://www.acmicpc.net/problem/1253
def search(s, e, index): # 두 포인터 : 양 끝에서부터 시작
  value = arr[index]
  while s < e:
    print(arr[:index])
    temp = (arr[s] + arr[e])
    # 인덱스 값이 같은 경우 위치 이동
    if temp > value or e == index: 
      e -= 1
    elif temp < value or s == index:
      s += 1
    else: # 해당 값인 경우 True 반환
      return True

if __name__=='__main__':
  N = int(input())
  arr = sorted(list(map(int,input().split())))
  res = 0
  if N > 2: # N이 2이하인 경우 자기 자신이 무조건 포함된다.
    for value in range(len(arr)):
      if search(0, len(arr)-1, value):
        res += 1
  print(res) # 정답 출력