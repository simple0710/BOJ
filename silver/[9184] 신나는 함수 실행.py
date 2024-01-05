# 2024/01/05 DP, Recursion
# https://www.acmicpc.net/problem/9184
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    # 하나라도 0이면 1반환
    if a <= 0 or b <= 0 or c <= 0: return 1
    # 하나라도 20을 넘기면 w(20, 20, 20) 반환
    elif a > 20 or b > 20 or c > 20: return w(20, 20, 20)
    # 해당 값이 저장되어 있다면 저장된 값을 반환한다.
    if dp[a][b][c]: return dp[a][b][c]
    # 주어진 조건에 따른 값을 저장하고, 반환한다.
    if a < b < c: dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else: dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

def main():
    while True:
        a, b, c = map(int,input().split())
        if (a, b, c) == (-1, -1, -1): break
        # 정답 출력
        print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

if __name__ == "__main__":
    main()