# 2023/04/30 Tree, Recursion
# https://www.acmicpc.net/problem/1991
def preorder_traversal(v): # 전위 순회
  if v == '.':
    return
  print(v, end='')
  preorder_traversal(data[v][0])
  preorder_traversal(data[v][1])

def inorder_traversal(v): # 중위 순회
  if v == '.':
    return
  inorder_traversal(data[v][0])
  print(v, end='')
  inorder_traversal(data[v][1])

def postorder_traversal(v): # 후위 순회
  if v == '.':
    return
  postorder_traversal(data[v][0])
  postorder_traversal(data[v][1])
  print(v, end='')

N = int(input())
data = dict()
for _ in range(N):
  m, s1, s2 = input().split()
  data[m] = [s1, s2]

# 정답 출력
preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')