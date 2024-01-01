# 2024/01/01 DataStructures, Hash-Set
# https://www.acmicpc.net/problem/7785
def main():
  n = int(input())
  res = set()
  for i in range(n):
    name, enterFlag = input().split(" ")
    res.add(name)
    # 회사를 떠난다면 집합에서 제외
    if (enterFlag == "leave"): res.remove(name)
  # 회사에 있는 사람 명단을 출력한다.
  # 이름 역순으로 출력한다.
  for i in sorted(res, reverse=True): print(i)

if __name__ == "__main__":
  main()