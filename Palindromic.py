#usr/bin/env python
#__coding:utf-8__

class Solution:
    def longestPalindrome(self, s):
        outString = ""
        while len(s) > len(outString):
            indLen = len(outString)
            temp = s[: indLen]
            # print("%%%%%%", temp)
            for ch in s[indLen:]:
                temp += ch
                if temp == temp[::-1]:
                    outString = temp if len(temp) > len(outString) else outString
            s = s[1:]
        return outString


if __name__ == "__main__":

    s = 'bdfgfd'
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)