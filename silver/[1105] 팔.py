L, R = input().split()
cnt = 0
# L과 R의 길이가 다를 경우 cnt가 0인 경우가 생길 수 밖에 없다.
if len(str(L)) != len(str(R)):
    print(cnt)
else:
    for i in range(len(str(L))):
        # 같지 않은 부분이 있다면 종료
        if L[i] != R[i]:
            break
        # 8이 있다면 cnt += 1
        else:
            if L[i] == '8':
                cnt += 1
    print(cnt)
