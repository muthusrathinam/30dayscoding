def postOrder(root):
    #Write your code here
    if(root):
        #Traverse to left of the root
        postOrder(root.left)
        #Traverse to right of the root
        postOrder(root.right)
        #print the node
        print(root, end=" ")