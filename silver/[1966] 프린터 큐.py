t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    # 문서 중요도
    imp = list(map(int,input().split()))
    # 인덱스
    idx = list(range(len(imp)))
    # 찾을 값
    idx[m] = 'target'
    cnt = 0
    while True:
        # 맨 처음 값이 최댓값인 경우
        if imp[0] == max(imp):
            cnt += 1
            # 맨 처음 인덱스가 타겟인 경우 출력 후 종료
            if idx[0] == 'target':
                print(cnt)
                break
            # 맨 처음 인덱스가 타겟이 아닌 경우 삭제
            else:
                imp.pop(0)
                idx.pop(0)
        # 맨 처음 값이 최댓값이 아닌 경우 마지막으로 보냄
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
