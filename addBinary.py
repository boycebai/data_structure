#usr/bin/env python
#__coding:utf-8__


class Solution:
    def addBinary(self, a, b):
        # tmp = 0
        # if len(a) > len(b):
        #     for i in range(len(b)-1, -1, -1):
        #         # print(i,a[i],b[i])
        #         tmp = a[i] + b[i]
        #         if tmp ==  2:
        #             print("###")
        #             a[i] = 0
        #             a[i - 1] = a[i - 1] + 1
        #     return a
        # elif len(b) > len(a):
        #     for i in range(len(a)-1, -1, -1):
        #         # print(i,b[i],a[i])
        #         tmp = b[i] + a[i]
        #         if tmp ==  2:
        #             print("###")
        #             b[i] = 0
        #             b[i - 1] = b[i - 1] + 1
        #     return b
        # else:
        #     for i in range(len(a)-1, -1, -1):
        #         # print(i,b[i],a[i])
        #         tmp = b[i] + a[i]
        #         if tmp ==  2 and i != 0:
        #             print("###")
        #             b[i] = 0
        #             b[i - 1] = b[i - 1] + 1
        #         elif tmp ==  2 and i != 0:
        #             b[i] = 0
        #             b = '1' + b
        #         else:
        #             b[i] = tmp
        #     return b

        sum = int(a,2) + int(b,2)
        ans = bin(sum)
        return ans[2:]



if __name__ == "__main__":

    a = "1111"
    b = "111"
    solution = Solution()
    result = solution.addBinary(a, b)
    print(result)