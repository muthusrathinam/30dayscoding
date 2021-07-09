def findMergeNode(head1, head2):
    #find the length of linked list
    def getcount(head):
        #since head val will not be None
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count
    
    #fn(diff, longlist, shortlist)
    def getnode(d, head1, head2):
        #traverse upto d
        for i in range(d):
            head1 = head1.next
        
        while head1 and head2:
            #check the common node
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next
    
    c1 = getcount(head1)
    c2 = getcount(head2)
    
    #check the difference
    if c1>c2:
        return getnode(c1-c2, head1, head2)
    else:
        return getnode(c2-c1, head2, head1)
