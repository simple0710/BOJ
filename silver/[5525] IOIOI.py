n = int(input())
m = int(input())
s = input()

result, i, cnt = 0, 0, 0

# 마지막 인덱스를 넘어서면 종료
while i < (m-1):
  # 'IOI' 와 같은 경우
  if s[i:i+3] == 'IOI':
    i += 2 # 인덱스 +2 (+1인 경우는 볼 필요 없다.)
    cnt += 1
    # cnt가 n과 같으면 result += 1, cnt -= 1(다음에도 같은 경우가 나올 경우 대비)
    if cnt == n:
      result += 1
      cnt -= 1
  # "IOI'와 다른 경우 인덱스를 추가하고 cnt를 초기화한다.
  else:
    i += 1
    cnt = 0

print(result)