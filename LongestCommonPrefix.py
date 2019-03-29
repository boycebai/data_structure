#usr/bin/env python
#__coding:utf-8__

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) > 0:
            cPrefix = strs[0]
            for substring in strs:
                shortestLength = len(cPrefix) if len(cPrefix) < len(substring) else len(substring)
                temp = ""
                for pos in range(shortestLength):
                    if cPrefix[pos] != substring[pos]:
                        break
                    else:
                        temp += cPrefix[pos]
                cPrefix = temp
            return cPrefix
        else:
            return ""

if __name__ == "__main__":

    strs = ["flower","flow","flight"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)