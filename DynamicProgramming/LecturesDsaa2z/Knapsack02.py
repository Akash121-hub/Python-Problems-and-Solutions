class Solution:
    def KnapSack(self,N,W,val,wt):
        dp = {}
        def solve(n,cap):
            if (n or cap) == 0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                cval = val[n-1]
                cwt = wt[n-1]
                if cwt <= cap:
                    choice1 = solve(n-1,cap-cwt)
                    choice2 = solve(n-1,cap)
                    c = max(choice1,choice2)
                else:
                    c = solve(n-1,cap)
                dp[(n,cap)] = c
                return c
        return solve(N,W)