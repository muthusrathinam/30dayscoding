def deleteNode(head, position):
    # Write your code here
    #position is head
    if position == 0:
        head = head.next
    else:
        #general case
        temp = head
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count += 1
        #delete the node
        temp.next = temp.next.next
    
    return head
    
