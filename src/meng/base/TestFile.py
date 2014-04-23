#!/bin/python
#coding=utf-8
import os

'''
Created on 2014年4月23日

@author: Administrator
'''
print("文件操作测试!!!")

# 文件操作可以使用内置的函数open来进行。
# open(文件名[,mode])返回一个文件对像。
# mode: "r",读模式"w"，写模式"r+"，读写模式
# 文件对像的方法:file.read(size)：读取文件的size个字节.返回一个string对象.
# 如果没有设置size,则读取整个文件。 file.readline():读取一行，返回一个string对象，如果返回的内容为空，则说明文件结束Eof。 
# file.readlines():读取所有的行，返回一个listfile.write(buffer)：写buffer的内容到文件.file.flush()强制写缓冲区的内容到文件
# file.seek(offset[,flag]):定位文件读写光标。 offset偏移量 flag标志：os.SEEK_SETor0从文件头算起，缺省的方式。
#  os.SEEK_CURor1从当前位置算起os.SEEK_ENDor2从结束处算起
#  file.close()关闭文件
#  文件对象的属性:file.name:文件名 file.mode:文件打开的模式

nowpath = os.getcwd()
fname = "t2.txt"
print fname
try:
    fobj = open(fname, 'w');
except IOError,e:
    print "file open error",e
else:
    txts =[];
    txts.append("tom 22")
    txts.append("sdfsadf 10")
    fobj.writelines(['%s%s' % (x, os.linesep) for x in txts])
    fobj.close()

try:
    f = open("t.txt", 'w')
except IOError,e:
    print "file open error",e
else:
    f.write("txt\n")
    f.write("dfasfjaskdfj")
    f.close()

#读取文件
print "读取文件====="    
f2 = open("t.txt", 'r')
try:
    f_content = f2.read();
except IOError,e:
        print "file open error",e
finally:
    f2.close();
print(unicode(f_content, 'UTF-8'))
    

