# 2022/12/06 그리디
# https://www.acmicpc.net/problem/1339
if __name__ == "__main__":
  N = int(input())
  words = []
  for _ in range(N):
    words.append(input())

  dict = {}
  for word in words:
    sr = len(word) - 1
    # 단어 확인
    for c in word:
      if c in dict:
        dict[c] += pow(10, sr)
      else:
        dict[c] = pow(10, sr)
      # 제곱근을 빼준다.
      sr -= 1

  # 큰 값부터 사용하기 위해 정렬
  dict = sorted(dict.values(), reverse=True)

  res = 0
  m = 9 # 최고 값부터 감소
  # 값 계산
  for value in dict:
    res += value * m
    m -= 1

  # 정답 출력
  print(res)