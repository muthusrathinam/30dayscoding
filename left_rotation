def rotateLeft(d, arr):
    # Write your code here
    arr = arr[d:] + arr[:d]
    return arr
    '''
    if d==len(arr):
        return arr
    
    for i in range(0,d):
        tmp = arr[0]
        for j in range(1,len(arr)):
            arr[j-1] = arr[j]
        arr[len(arr)-1] = tmp
    
    return arr
'''
'''
    tmp = [None] * d
    for i in range(d):
        tmp[i] = arr[i]
    for j in range(n-d):
        arr[j] = arr[j+d]
    for k in range(d):
        arr[k+n-d] = tmp[k]
    return arr
'''
    
