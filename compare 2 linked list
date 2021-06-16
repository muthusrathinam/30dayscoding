def compare_lists(head1, head2):
    ptr1 = head1
    ptr2 = head2
    
    #while ptr1 != None and ptr2 != None:
    while ptr1 and ptr2:
        #check wheather the data are same
        if ptr1.data == ptr2.data:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        else:
            return 0
    
    if ptr1 == None and ptr2 == None:
        return 1
    else:
        return 0
