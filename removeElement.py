#usr/bin/env python
#__coding:utf-8__


class Solution:
    def removeElement(self,nums,val):
        # list = []
        nums.remove(val)
        return len(nums)

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 2
    solution = Solution()
    result = solution.removeElement(nums,val)
    print(result)