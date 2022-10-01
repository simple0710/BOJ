import sys
sys.setrecursionlimit(10000)

# 백트래킹
def back():
  global first, last, check
  # 해당 길이에 도달했다면 부등호 비교
  if len(s) == n + 1:
    result = list()
    for i in range(n):
      # 조건에 만족하면 result에 추가
      if data[i] == '>' and s[i] > s[i+1]:
        result.append(s[i])
      elif data[i] == '<' and s[i] < s[i+1]:
        result.append(s[i])
      # 조건에 맞지 않으면 종료
      else:
        return
    # 마지막 부분은 추가되지 않으므로 직접 추가
    result.append(s[-1])

    # 맨 처음의 결과 값(최솟값)은 first에 추가 후 check 값 변경
    if check == 0:
      first = result
      check = 1
    # 끝까지 출력했을 때 
    # 마지막으로 정의 되는 것이 최댓값이므로 계속 변경
    last = result
    return 

  for i in range(10):
    if i not in s:
      s.append(i)
      back()
      s.pop()

# 데이터 입력
n = int(input())
data = list(map(str, input().split()))

# 정의
s = list()
first = list()
last = list()
check = 0

back()

print(''.join(map(str, last)))
print(''.join(map(str, first)))
