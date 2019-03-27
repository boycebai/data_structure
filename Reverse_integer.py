#usr/bin/env python
#__coding:utf-8__

class Solution:
    def reverse(self, x):

        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        ans = 0

        while x:
            ans = ans * 10 + x % 10
            x = x / 10

        print(ans,2**31 - 1,ans * sign)
        if ans <= 2**31 - 1:
            return ans * sign
        else:
            return 0

if __name__ == "__main__":

    x = 3453462112
    solution = Solution()
    result = solution.reverse(x)
    print(result)
