# 2023/06/06 Math, Greedy
# https://www.acmicpc.net/problem/1049
N, M = map(int,input().split())
package_g = []
one_g = []
for _ in range(M):
  brand = list(map(int, input().split()))
  package_g.append(brand[0])
  one_g.append(brand[1])

package = min(package_g) # 패키지 최솟값
one = min(one_g) # 낱개 최솟값

if package > one * 6: # 낱개가 이득인 경우
  res = one * N
else: # 패키지가 이득인 경우
  res = N // 6 * package + min(package, one * (N % 6))
# 정답 출력
print(res)