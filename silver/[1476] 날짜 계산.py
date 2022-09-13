E, S, M = map(int,input().split())

day = [1,1,1]

cnt = 0
while True:
    cnt += 1
    # 만약 입력값과 같다면 종료
    if E == day[0] and S == day[1] and M == day[2]:
        break
    # 각 변수에 1을 추가
    for i in range(3):
        day[i] += 1
    # 특정 수를 넘으면 1로 돌아간다.
    if day[0] > 15:
        day[0] = 1
    if day [1] > 28:
        day[1] = 1
    if day[2] > 19:
        day[2] = 1
print(cnt)
