def recur(ind, hp, feel):
  global result
  # 체력이 초과 될 경우
  if hp >= 100:
    # 이전 행복도를 가져온다
    nf = feel - happy[ind-1]
    # 이전 행복도와 결과를 비교해서 큰 값이 출력된다.
    if nf > result:
      result = nf
    return result
  # 끝 부분에 도달했을 경우
  if ind == n:
    # result가 feel보다 작은 경우 result = feel
    if feel > result:
      result = feel
    return result
  # 다음 값을 더한 경우와 더하지 않은 경우로 재귀를 실행한다.
  recur(ind+1,hp+health[ind],feel+happy[ind])
  recur(ind+1,hp,feel)

n = int(input())
health = list(map(int,input().split()))
happy = list(map(int,input().split()))
result = 0

recur(0,0,0)
print(result)