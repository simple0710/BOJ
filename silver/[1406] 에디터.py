import sys

input = sys.stdin.readline
st1 = list(input().rstrip())
st2 = []
# 두 개의 리스트로 커서를 표현한다.
for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    # 제거
    elif command[0] == 'B':
        if st1:
            st1.pop()
    # 추가
    else:
        st1.append(command[1])
# 전부 실행하고 남는 st2를 st1에 추가한다.
st1.extend(reversed(st2))
print(''.join(st1))
