n = int(input())
top = list(map(int,input().split()))
stack = []
answer = [0] * n

for i in range(n):
  # 스택이 있는 경우
  while stack:
    # 이전 탑의 길이가 더 길다면 송신되는 것이므로 인덱스 값을 준다.
    if stack[-1][1] > top[i]:
      answer[i] = stack[-1][0] + 1
      break
    # 송신이 안된다는 뜻이므로 pop을 수행한다
    else:
      stack.pop()
  # 다음 탑의 인덱스 값과 길이를 추가한다.
  stack.append([i, top[i]])

print(' '.join(map(str,answer)))