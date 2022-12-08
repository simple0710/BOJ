# 2022/11/28 백트래킹
import copy

# 제출 정답 1
def back(end):
  global res
  # 처음과 끝을 제외한 값을 추가하였을 때
  if len(s) == N - 2:
    ener = 0
    # 새로운 데이터를 생성
    n_data = copy.deepcopy(data)
    # 해당 인덱스에서 나오는 합을 계산한다.
    for idx in s:
      ener += n_data[idx-1] * n_data[idx+1]
      n_data.pop(idx)
    # res와 비교해 큰 값을 res로 한다.
    res = max(res, ener)
    return

  # 순서를 구한다.
  for i in range(1, end):
    s.append(i)
    back(end - 1)
    s.pop()

# 정답 2, su에 0을 넣고 시작한다.
def back_2(su):
  global res
  # 다 모은 경우
  if len(data) == 2:
    # res와 비교해 큰 값을 res로 한다.
    res = max(res, su)
    return

  for i in range(1, N - 1):
    # 해당 인덱스에서 구할 수 있는 수
    t = data[i-1] * data[i+1]
    
    v = data.pop(i) # 구슬 제거
    back_2(su + t)
    data.insert(i, v) # 구슬 추가
    
# 정보 입력
N = int(input())
data = list(map(int,input().split()))
s = []
res = 0

# 백트래킹 시작
back(N - 1)

# 정답 출력
print(res)