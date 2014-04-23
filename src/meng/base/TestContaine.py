#!/bin/python
#coding=utf-8
'''
Created on 2014年4月23日

@author: Administrator
'''
# print("测试中  ! 容器");
# 容器就是用来存放一些对像的数据结构。根据使用方式的不同，python提供了列表（List）,元组（trupe）,字典（dict）

# 用来动态的存放对像，可以插入，删除，更新。使用[]来给表示，看上去像c的数组，
# 用起来像java的list(不是很准确，更像vector,不做过多解释)
# .定义：变量a=[]#空的列表或者变量b=[1,3,4,5,'iloveyou']
# #有值的列表，元素可以是不同的类型， 这和c，java都不一样。添加元素：a.append(元素) 
# #添加元素到最后 插入元素：a.insert(位置，元素)#在固定位置，插入元素，原来后面的元素往后排，
# 如果位置大于列表当然的长度，则后append的结果是一样的，添加到最后。列表是从0开始计数的，即第1个元素的索引是0
# 删除元素：a.remove(元素)
#从0开始索引，直到匹配到相等的第一个元素，删掉该元素。只会删除一个。 
# 索引元素：a.index(元素，开始，结束)
#返回匹配到的第一个元素的索引。 引用元素：a[索引]
# 遍历列表：

def listprint(b):
    '''
    函数名:listprint
    '''
    for f in b:
        if f != '.':
                print f
# end fun listprint

a=[1,2,3,4,5]
for v in a:
    print v
print("===a[0]====")
print a[0]

print("====a.remove(3)===")
a.remove(3)
listprint(a)  #调用函数

print("====a.append(3)===")
a.append(100)
listprint(a)  #调用函数

print("====a.insert(2,50)===")
a.insert(2, 50)
listprint(a)  #调用函数

# 元组和列表很相似，唯一的区别是元组定义好之后，就不能再改动了。所以元组简单很多。
# 定义： 变量a=(元素1，元素2，元素3...)
print("====元组===")
a2=(1, 2, 'sdfsf')
print a2
print("====元组 a2[1]===")
print a2[1]
print("====元组与字符串===")
print 'li li li %s,%d'%('my', 12)

# 字典就像是java中的map,根据一个键来对应一个对像。
# 定义： （1）变量a={} （2）变量a={key1:value1,key2:value2}
ab = { 'test1' : 'value11111',
      'test2' : 'value22222',
      'test3' : 'value33333',
      'test4' : 'value44444'
      }
print("====字典===")
print "sdfasdfasdf' address is %s" % ab['test1']
print("====字典设置值:===")
ab['test2'] = "88888"
print ab
del ab['test4']
print("====del ab['test4']:===")
print ab
print("====len(ab)===")
print len(ab)
print("====for循环===")
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)
print("====判断是否存在===")
if 'test2' in ab: # OR ab.has_key('test2')
    print "test2's address is %s" % ab['test2']
else:
    print "不存在！！"
    
# 列表、元组和字符串都是序列，但是序列是什么，它们为什么如此特别呢？序列的两个主要特点是索引操作符和切片操作符。
# 索引操作符让我们可以从序列中抓取一个特定项目。切片操作符让我们能够获取序列的一个切片，
# 即一部分序列。
print("序列方面")
c = 'Iloveyou'
print c
print("c = 'Iloveyou' c[0]")
print c[0]
print("c[0:1] 后面的那个不包括本身")
print c[0:1]
print("c[0:2]")
print c[0:2]
print("c[5:]")
print c[5:]
print("c[:-1]")
print c[:-1]

