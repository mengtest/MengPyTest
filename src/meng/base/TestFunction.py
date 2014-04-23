#!/bin/python
#coding=utf-8
'''
Created on 2014年4月23日

@author: Administrator
'''
print("测试中  ! 函数");

# 格式： def函数名（参数，参数）： 
# 实现语句
# 实现语句
# 实现语句retrun... 
# 最后缩进结束，代表函数结束。

def sayhello(count):
    '''
    函数名:sayhello
    参数:count
    '''
    for j in range(count):
        print "hello!"
# end fun sayhello

sayhello(5) #调用函数

# 注意： 1参数，和return语句都不是必须的
# 2缩进需要注意
# 3局部变量 函数内部使用的变量，不影响外部的变量，即使变量同名。
# 4全局变量 全局变量就是在所以函数外部定义的变量。函数内部可以使用全局变量，但要使用global声明。

id=1000
def addandprintId():
    '''
    函数名:addandprintId
    '''
    global id
    print id
    id = id+1
# end fun addandprintId
addandprintId() #调用函数 1000
addandprintId() #调用函数 1001
addandprintId() #调用函数 1002

# 常用内置函数
# ranwinput([prompt])
# 用来让用户输入数据。prompt是提示，可以不要。 注意：SPE的ide里没有提供输入的界面，所以要有这个功能要在dos控制台中执行?
# int() 用来返回整数，可以将string类型转化成int类型。

a = raw_input("请输入数值:")
if int(a)>100:
    print a
else:
    print "小于100"
    
#     len([string])
# 用来计算字符串，列表等对像的长度。
print len('intsdfaf')
# 注意：很多程序员喜欢用len做为变量来表示长度，在python是不行了，因为len已经是一个内置的函数了。

# str() 将对像转化成字符串
print str(1000)

    