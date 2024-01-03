# 2024/01/03 DataStructures, Stack
# https://www.acmicpc.net/problem/17299
def solution(N, data):
  cntDict = {}
  # 개수 파악
  for i in data: cntDict[i] = cntDict.get(i, 0) + 1
  res = [-1] * N
  stack = [0]
  for i in range(1, N):
    # 현재 stack에 값이 있고,
    # 스택의 마지막에 있는 인덱스에 해당하는 값의 개수보다 현재 위치의 개수가 더 많은 경우
    while stack and cntDict[data[stack[-1]]] < cntDict[data[i]]:
      # 해당 인덱스 제거 및 값 갱신
      res[stack.pop()] = data[i]
    stack.append(i) # 현재 인덱스 추가
  return res # 정답 반환

def main():
  N = int(input())
  data = list(map(int,input().split()))
  print(*solution(N, data)) # 정답 출력

if __name__ == "__main__":
  main()