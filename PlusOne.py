#usr/bin/env python
#__coding:utf-8__


class Solution:
    def plusOne(self,digits):
        if digits[-1] < 9:
                digits[-1] += 1
                return digits
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] >= 9 and i > 0:
                    digits[i] = 0
                    digits[i - 1] += 1
                    if digits[i - 1] <= 9:
                        return digits
                elif digits[i] > 9 and i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                elif digits[i] == 9 and i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                else:
                    return digits
            return digits




if __name__ == "__main__":
    digits = [9]
    # digits = [5,2,2,6,5,7,1,9,0,3,8,6,8,6,5,2,1,8,7,9,8,3,8,4,7,2,5,8,9]#[9]
    solution = Solution()
    result = solution.plusOne(digits)
    print(result)