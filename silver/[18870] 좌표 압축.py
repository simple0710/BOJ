# 2022/11/20 값/좌표 압축
import sys
input = sys.stdin.readline

# 길이와 숫자 입력
n = int(input())
numbers = list(map(int,input().split()))

# 중복되지 않는 집합 생성
setlist = set(numbers)
# 리스트로 만든 후 정렬
a = list(setlist)
a.sort()

# 딕셔너리에 해당 값에 인덱스 지정
numdict = {}
for i in range(len(a)):
  numdict[a[i]] = i

# 정답 출력
for i in numbers:
  print(numdict[i], end = ' ')