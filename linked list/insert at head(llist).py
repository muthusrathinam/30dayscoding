def insertNodeAtHead(head, data):
    # Write your code here
    #create the new node
    node = SinglyLinkedListNode(data)
    
    if head != None:
        node.next = head
    
    return node
    
