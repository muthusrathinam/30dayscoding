def reverse(head):
    # Write your code here
    while head.next != None:
        #swap the pointers
        head.next, head.prev,head = head.prev, head.next, head.next
        
    #change to the tail node
    head.next, head.prev = head.prev, None
    
    return head
