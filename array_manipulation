def arrayManipulation(n, queries):
    # Write your code here
    #initializing the array with zeroes
    arr = [0] * (n+2)
    
    #perform the query operation 
    for a,b,k in queries:
        arr[a] += k
        arr[b+1] -= k
        
    #find max elem in array
    max_num = temp = 0
    for val in arr:
        temp += val
        max_num = max(max_num, temp)
        
    return max_num
    
