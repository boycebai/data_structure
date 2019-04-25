#usr/bin/env python
#__coding:utf-8__

'''
问题:有1到50个数组成的集合,每次随机取出两个数(不放回),把这
两个数相减的绝对值放回集合,这样操作49次后,剩下的数最有可能是几?
Author:Chunshan Bai
Date:2019-04-25
如有引用,请申明作者姓名!
'''


import random

def question(str):
    #随机选择两个数
    num_1 = random.choice(str)
    str.remove(num_1)
    num_2 = random.choice(str)
    str.remove(num_2)
    #两数的差的绝对值
    tmp = abs(num_1 - num_2)
    str.append(tmp)
    return str

def all_list(arr):
    #统计数组中每个数字的个数
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


if __name__ == "__main__":

    n = 100000 #试验次数(可更改)
    list = []
    for j in range(1, n + 1):
        #构建1到50个数
        str = []
        for i in range(1,51):
            str.append(i)
        # print(str)
        #取49次值
        for k in range(1,50):
            result = question(str)
        list.append(result[0])
    result = all_list(list)

    print(result) #输出对应元素次数表


