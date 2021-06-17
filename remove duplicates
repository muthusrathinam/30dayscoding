def removeDuplicates(head):
    # Write your code here
    #create temp poiters
    temp = head
    
    while temp.next != None:
        if temp.data == temp.next.data:
            #this delete the next node
            temp.next = temp.next.next
            
        else:
            temp = temp.next
    
    return head
