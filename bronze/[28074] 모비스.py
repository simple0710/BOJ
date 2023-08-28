# 2023/06/25 Implementation, String
# https://www.acmicpc.net/problem/28074
string = input()
for i in ["M", "O", "B", "I", "S"]: # 확인
  if i not in string or len(string) < 5: # MOBIS가 문자열 안에 없거나, 길이가 5 이하인 경우
    print("NO")
    break
else: # MOBIS를 만들 수 있는 경우
  print("YES")