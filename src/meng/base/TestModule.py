#!/bin/python
#coding=utf-8
'''
Created on 2014年4月23日

@author: Administrator
'''

# import TestFunction
import sys
import time
import md5
import random

print("测试中  ! 模块");

# 模块是现代程序组织中所不可少的，每一个.py文件就是一个模块。
# 每个一模块实现相对独立功能，当需要使用这个模块时只要通过import指令导入即可，而不需要都去造一个相同"轮子"。
#  import模块名 使用模块提供的对像时需要加上模块名 （python所有东西都是对象，如变量，函数等等）

a=2
# TestFunction.sayhello(a)

# 注意：自己写的模块(.py文件)一定不要与系统自带的模块重名，除非你想替代系统模块。因为你的运行路径放在了第一的位置。
# from模块名import*或from模块名import对象可以直接使用模块提供的对象。
# 使用dir(模块名)可以查看，模块提供的对象。
# print("dir(TestFunction)")
# print dir(TestFunction)

# 常用的标准模块 sys
# sys.argv程序的入口参数，是一个列表
# sys.path装载模块的搜索路径，是一个列表
# sys.versionpython的版本，是一个string
# sys.exit(status)退出程序,是一个函数
# 注意：自己写的模块(.py文件)一定不要与系统自带的模块重名，除非你想替代系统模块。因为你的运行路径放在了第一的位置。
print("常用的标准模块 sys")
print(sys.argv)
print("sys.path")
print(sys.path)

# time
# time.sleep(n)休息n秒，可以是小数
# time.time()返回一个浮点数，从1970-1-1，0：0：0到当前绝对时间的秒数，还有8位的小数
# time.localtime(second)返回一个元组,如果没有second,就使用time.time()返回的秒，
# time.strftime(format)格式
# time.strftime('%Y-%m-%d%H:%M:%d')
print("time====")
print time.strftime('%Y-%m-%d%H:%M:%d')

# os
# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'， 而对于Linux/Unix用户，它是'posix'。
# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
# os.listdir()返回指定目录下的所有文件和目录名。
# os.remove()函数用来删除一个文件。
# os.system()函数用来运行shell命令。

# md5
# ·md5.new(arg) arg要md5的内容，返回一个md5对象
# ·digest(),摘要，返回16个字节 
# · hexdigest(),16进制摘要，返回32个字节
print("md5=====")
m = md5.new("testcom")
print m.digest()
print m.hexdigest()

# random
print("random====")
print("#Randomfloatx,0.0<=x<1.0")
print random.random()
print("Randomfloatx,1.0<=x<10.0")
print random.uniform(1, 10)
print("#Integerfrom1to10,endpoints")
print random.randint(1, 10)
print("#Evenintegerfrom0to100")
print random.randrange(0, 101, 2)
print("#Choosearandomelement")
print random.choice("abcdefghij")
print("random.shuffle(items)")
items = [1, 2, 5, 7, 9]
random.shuffle(items)
print items
print("random.sample（） choose 3 elements")
print random.sample([1,2,3,4,5], 3)
