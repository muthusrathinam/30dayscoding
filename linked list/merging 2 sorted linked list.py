#use this below line to avoid runtime errors
#sys.setrecursionlimit(100000)

def mergeLists(head1, head2):
    #both the lists are empty
    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    temp = None
    if head1.data < head2.data:
        #assign smaller data to temp ptr
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
    
    return temp
