#!/bin/python
#coding=utf-8
'''
Created on 2014年4月23日

@author: Administrator
'''

print("测试中  !");

# a="xiao's book"
# b='dfasfasf'
# print a
# print b

# 有两点要注意：
# 1语句后面有:号
# 2子句要缩进
# a = 16;
# if a>10:
#     print "a>=10"
# elif a > 15:
#     print "a>=15"
# else:
#     print "a<=XXX"

#内置函数range(起始值，终止值，步长)
#起始值缺省是0,可以不写
#步长值缺省是1，可以不写
#终止值是采用小于，而不是小于等于，所以是满足条件的是不包括终止值。
for i in range(5):
    print i
