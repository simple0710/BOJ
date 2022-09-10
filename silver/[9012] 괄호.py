for _ in range(int(input())):
    word = input()
    while True:
        word = word.replace('()','')
        # '(' 밖에 안 남으면 종료
        if '(' not in word:
            break
        # ')' 밖에 안 남으면 종료
        elif ')' not in word:
            break
        # 양쪽 끝이 ),( 이면 종료
        if word[0] == ')' or word[-1] == '(':
            break
    if word:
        print('NO')
    else:
        print('YES')
