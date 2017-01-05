#!/usr/bin/python
# -*- coding: utf-8 -*-


#python的数据类型包括整数\浮点数\字符串\布尔值\空值None
print(4567+0x12fd2)
print 4567+0x12fd2

#字符串输出使用""或''扩住,不做计算直接输出
print("Learn Python in imooc")
print 'Hello,World'
print "Hello World"

print(100<99)

print(0xff==255)

#print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出
print '我的名字','是','黄丽娟'


print "hello,python"
print 'hello,','python'

#求等差数列1 4 7 10……前100项的和
x1 = 1
d = 3
n = 100
x100 = x1 + (n-1)*d
s = n*(x1+x100)/2
print s