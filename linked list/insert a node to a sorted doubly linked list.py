def sortedInsert(head, data):
    # Write your code here
    #create a new node
    node = DoublyLinkedListNode(data)
    
    #case1: list is empty
    if head == None:
        head = node
        
    #case2: insert before head
    elif data < head.data:
        node.next = head
        head.prev = node
        head = node
        
    #case3: insert at specific position or at the end
    else:
        cur = head
        #traverse to the specific position
        while cur.next != None and cur.data < data:
            cur = cur.next
        
        #insert at the end
        if cur.next == None and cur.data < data:
            cur.next = node
            node.prev = cur
        
        #insert at specific position
        else:
            previous = cur.prev
            #make changes to the previous node
            previous.next = node
            node.prev = previous
            #make changes for current node
            node.next = cur
            cur.prev = node
        
    return head
