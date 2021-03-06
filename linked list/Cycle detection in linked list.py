approach 1 : optimized using only 2 ptr's

***************Floyd’s Cycle-Finding Algorithm******************* 

def has_cycle(head):
    #initialize two pointers
    fast = slow = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        #checks for allocated memory is same or not for the two ptr's
        #simply checks if both ptr is same
        if slow == fast:
            return True
    
    return False

approach 2(using hash) #it takes extra space to store values in hashmap

def has_cycle(head):
    s = set()
    temp = head
    while (temp):

        # If we have already has
        # this node in hashmap it
        # means their is a cycle
        # (Because you we encountering
        # the node second time).
        if (temp in s):
            return True

        # If we are seeing the node for
        # the first time, insert it in hash
        s.add(temp)

        temp = temp.next

    return False
