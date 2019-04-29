#usr/bin/env python
#__coding:utf-8__


class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        if (len(s) > 0):
            s = s.split()
            return len(s[-1])
        else:
            return 0


if __name__ == "__main__":

    s = "Hello World "

    solution = Solution()
    result = solution.lengthOfLastWord(s)
    print(result)