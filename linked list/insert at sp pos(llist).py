def insertNodeAtPosition(head, data, position):
    # Write your code here
    node = SinglyLinkedListNode(data)
    
    #head pointer is null
    if head == None:
        head = node
    else:
        tmp = head
        #skip the nodes to reach positions
        count=1
        while tmp != None and count < position:
            tmp = tmp.next
            count += 1
        
        #insert the node after reaching the pos
        node.next = tmp.next
        tmp.next = node
    
    return head
    
