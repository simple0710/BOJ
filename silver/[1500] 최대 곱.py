s, k = map(int,input().split())

data = list()
# s를 k등분 한다.
for i in range(k):
    p = s//k
    data.append(p)

# 만약 총 합이 부족하다면 순서대로 +1
a = 0
while sum(data) < s:
    data[a] += 1
    a += 1
    if a == k:
        a = 0
        
# 모든 값을 곱하여 출력한다.       
result = 1    
for i in data:
    result *= i
print(result)
