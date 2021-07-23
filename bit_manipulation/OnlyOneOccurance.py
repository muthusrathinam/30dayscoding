def xor(arr, n):
  ans = arr[0]
  
  for i in range(1,n):
    ans = ans ^ arr[i]
    
  return ans

T = int(input())

for test in range(T):
  N = int(input())
  list_n = list(map(int, input().split()[:N]))
  
  res = xor(list_n, N)
  
print(res)

'''
Input
1
9
1 2 3 4 5 4 3 2 1

Output
5
'''