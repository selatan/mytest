#!/usr/bin/python
# -*- coding: utf-8 -*-
#import math
# from math import pow,sin,log
#
# print pow(2,3)

# class Person():
#     pass
#
# xiaoming = Person()
# xiaohong = Person()
#
# print xiaoming
# print xiaohong
# print xiaoming==xiaohong

# class Person(object):
#     pass
#
# p1 = Person()
# p1.name = 'Bart'
#
# p2 = Person()
# p2.name = 'Adam'
#
# p3 = Person()
# p3.name = 'Lisa'
#
# L1 = [p1, p2, p3]
# L2 = sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))
#
# print L2[0].name
# print L2[1].name
# print L2[2].name


# #请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
# #要定义关键字参数，使用 **kw；除了可以直接使用self.name = 'xxx'设置一个属性外，还可以通过 setattr(self, 'name', 'xxx') 设置属性。
# class Person(object):
#     def __init__(self,name,gender,birth,**kw):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         for k,v in kw.iteritems():
#             setattr(self,k,v)
#
# xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
#
# print xiaoming.name
# print xiaoming.job



#
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#         self._title = 'Mr'
#         self.__job = 'Student'
# p = Person('Bob')
# print p.name
# print p._title
# print p.__job



class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
