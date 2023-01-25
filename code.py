class Solution:
    def addToArrayForm(self, A: List[int], K: int): 
        ans, i = [], len(A) - 1 #First (len(A)-1) parameter means our loop will start from end of the array A[]
        while K > 0 or i >= 0: # loop through A and K, from right to left.
            K, rmd = divmod(K + (A[i] if i >= 0 else 0), 10) #Use K as carry over, and add A[i].
#takes two numbers as parameters and gives the quotient and remainder of their division as a tuple
#K, a = divmod(K, 10)''' means that K, a = (K / 10, K % 10).
            ans.append(rmd) # add the least significant digit of K
            i -= 1
        return reversed(ans)
