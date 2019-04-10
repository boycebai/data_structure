#usr/bin/env python
#__coding:utf-8__


class Solution:
    def myAtoi(self,str):
        from string import digits
        res = list()
        str = str.strip()

        flag = 1
        if len(str) > 0:
            if str[0] == '-':
                flag = -1
                str = str[1:]
            elif str[0] == '+':
                flag = 1
                str = str[1:]
        if str == '' or str[0] not in digits:
            return 0
        for x in str:
            if x in digits:
                res.append(x)
            else:
                 break
        res =  int(''.join(res)) * flag
        if flag == 1:
            if res > (1<<31) -1:
                return (1<<31) -1
            else:
                return res
        else:
            if res < -(1<<31):
                return -(1<<31)
            else:
                return res

if __name__ == "__main__":

    str = ' -678 on word'
    solution = Solution()
    result = solution.myAtoi(str)
    print(result)