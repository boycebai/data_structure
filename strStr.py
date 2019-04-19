#usr/bin/env python
#__coding:utf-8__


class Solution:
    def strStr(self, haystack, needle):

        if len(needle) == 0:
            return 0

        for i in range(0,len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1



if __name__ == "__main__":

    haystack = "hello"
    needle = "ll"
    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)