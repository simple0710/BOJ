n = int(input())
m = int(input())
s = input()

# IO의 n번 곱한 후 I를 더한 문자열 생성
p_data = 'IO' * n +'I'

cnt = 0
for j in range(m-len(p_data)):
  # 만약 해당 부분이 p_data와 같으면 cnt += 1
  if s[j:j+len(p_data)] == p_data:
    cnt += 1

print(cnt)
