# 2023/12/29 Math
# https://www.acmicpc.net/problem/4299
def main():
  a, b = map(int,input().split())
  x = (a + b) // 2
  y = (a - b) // 2
  # a가 더 커야 x, y를 구할 수 있다.
  if a >= b and x + y == a and x - y == b: print(x, y)
  else: print(-1)
  
if __name__ == "__main__":
  main()