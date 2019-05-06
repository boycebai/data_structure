#usr/bin/env python
#__coding:utf-8__

class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        temp1,temp2=1,1
        for i in range(2,n+1):
            temp1,temp2=temp2,temp1+temp2
            print("**************")
            print(temp1,temp2)
        return temp2



if __name__ == "__main__":

    n = 6
    solution = Solution()
    result = solution.climbStairs(n)
    print("result", result)