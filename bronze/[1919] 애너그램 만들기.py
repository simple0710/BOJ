# 2023/12/01 Implementation, String
# https://www.acmicpc.net/problem/1919
def main():
  a = input()
  b = input()
  cnt_dict = dict()
  # 문자 개수 탐색
  for i in a: cnt_dict[i] = cnt_dict.get(i, 0) + 1
  for i in b: cnt_dict[i] = cnt_dict.get(i, 0) - 1
  # 각각의 문자 차이의 합
  res = sum([abs(i) for i in cnt_dict.values()])
  print(res) # 정답 출력

if __name__ == '__main__':
  main()