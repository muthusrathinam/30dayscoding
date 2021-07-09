'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    #make sure v1 is lesser and v2 is greater
    if v1>v2:
        v1, v2 = v2, v1
        
    #main logic
    while True:
        #if both values are lesser
        if v1 < root.info and v2 < root.info:
            root = root.left
        #if both values are greater 
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root
  
