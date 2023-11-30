# 2023/11/30 Implementation, String
# https://www.acmicpc.net/problem/11328
def main():
  N = int(input())
  for _ in range(N):
    a, b = input().split()
    # strfry 함수 적용이 가능한 경우 Possible 출력
    if sorted(a) == sorted(b): print('Possible')
    # strfry 함수 적용이 불가능한 경우Impossible 출력
    else: print('Impossible')

if __name__ == "__main__":
  main()