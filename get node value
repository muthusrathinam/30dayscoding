def getNode(head, positionFromTail):
    # Write your code here
    ptr1 = head
    ptr2 = head
    
    #traverse to the position(k)from the head
    for i in range(positionFromTail):
        ptr1 = ptr1.next
    
    #traverse both pointers
    while ptr1.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr2.data
