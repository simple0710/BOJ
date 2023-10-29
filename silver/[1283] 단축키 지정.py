# 2023/08/20 Implementation, String
# https://www.acmicpc.net/problem/1283
import sys
input = sys.stdin.readline

def solution(N, data):
  check = []
  for i in range(N):
    for j in range(len(data[i])): # 각 단어의 첫글자를 확인
      if data[i][j][0].upper() not in check: # 첫글자가 단축키로 쓰이지 않은 경우
        check.append(data[i][j][0].upper())
        data[i][j] = f'[{data[i][j][0]}]{data[i][j][1:]}'
        break
    else:
      new_string = ' '.join(map(str, data[i]))
      for idx, j in enumerate(new_string): # 모든 문장 확인
        if j != ' ' and j.upper() not in check: # 단축키로 사용되지 않은 알파벳이 있는 경우
          new_string = f'{new_string[:idx]}[{new_string[idx]}]{new_string[idx+1:]}'
          check.append(j.upper())
          data[i] = [new_string]
          break
  return data # 정답 반환

def main():
  N = int(input())
  data = [list(map(str, input().rstrip().split())) for _ in range(N)]
  res = solution(N, data) # 탐색 시작
  for i in res: # 정답 출력
    print(' '.join(map(str, i)))

if __name__ == "__main__":
  main()