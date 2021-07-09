def reversePrint(head):
    # Write your code here
    #initialize three pointers
    prev = None
    cur = head
    nxt = head.next
    
    while cur != None:
        nxt = cur.next
        #change the direction of the nodes
        cur.next = prev
        #shifting the nodes
        prev = cur
        cur = nxt
    
    head = prev
    
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next

    

'''
    if (head != None):
        reversePrint(head.next)
        print(head.data)
'''
