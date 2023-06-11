class Solution:
    def fib(self, n: int) -> int:
        if n<0: return n
        if n==0 : return 0
        if n==1: return 1   
        #recursion return self.fib(n-1)+ self.fib(n-2)
        output, prev1, prev2 = 0,1,0
        for i in range(2, n+1):
            output = prev1 + prev2
            prev2 = prev1
            prev1 = output
        return output