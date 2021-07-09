def printLinkedList(head):
    #create a temporary pointer
    temp = head
    
    #print elements in the linked list
    while temp != None:
        #print from head data
        print(temp.data)
        #move to next pointer
        temp = temp.next
        
