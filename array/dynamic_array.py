# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seq_list = [[] for i in range(n)]  #created N empty lists
    last_answer = 0
    res = []
    for q in queries:
        #case 1
        if q[0]==1:
            seq=(q[1] ^ last_answer)%n # ^ is xor operator
            seq_list[seq].append(q[2]) #append y
        #case 2
        else:
            seq=(q[1] ^ last_answer)%n
            y = q[2]%len(seq_list[seq])     # y % seq_size
            last_answer = seq_list[seq][y]
            res.append(last_answer)
        
    return res
    
