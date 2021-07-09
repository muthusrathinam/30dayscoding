def preOrder(root):
    #Write your code here
    if root != None:
        #print the node
        print(root, end=" ")
        #traverse to the left of root node
        preOrder(root.left)
        #traverse to the right of root node
        preOrder(root.right)