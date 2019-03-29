#usr/bin/env python
#__coding:utf-8__


class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        temp = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[temp]:
                temp += 1
                nums[temp] = nums[i]
        return temp+1

if __name__ == "__main__":

    nums = [1,1,2]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print(result)