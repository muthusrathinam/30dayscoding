def decodeHuff(root, s):
	#Enter Your Code Here
    #create temp. pointer
    temp = root
    result=[]
    
    #traverse binary coded string
    for char in s:
        #traverse left of the tree
        if char is '0':
            temp = temp.left
        #traverse right of the tree
        else:
            temp = temp.right
        
        if temp.left is None and temp.right is None:
            result.append(temp.data)
            temp = root
    
    print("".join(result))
    