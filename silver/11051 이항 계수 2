import sys

n, k = map(int,input().split())

result = 1
div = 1

for i in range(k):
    result *= n
    n -= 1
    
for i in range(2,k+1):
    div *= i
print((result//div)%10007)
