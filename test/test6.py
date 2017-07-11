#!/usr/bin/python
# -*- coding: utf-8 -*-

# a=1
# def fun(a):
#     a=2
# fun(a)
# print a
#
#
#
# s=set(['Adam','Lisa','Paul'])
# L=['Adam','Lisa','Bart','Paul']
# for x in L:
#     if x in s:
#             s.remove(x)
#     else:
#         s.add(x)
#
# print s

# def fact(n):
#     if n==1:
#         return 1
#     return fact(n-1)*n
# print fact(5)


# L=range(1,101)
# print L
# print L[-10:]

# L = ['Adam','Lisa','Bart','Paul']
# print L[-2:-1]

# def firstCharUpper(s):
#      return s[0:1].upper()+s[1:]
# print firstCharUpper('hello')
# print firstCharUpper('sunday')
# print firstCharUpper('september')


# for i in range(1,101):
#     if i%7==0:
#         print i

# #匿名函数
# print map(lambda x:x*x,[1,2,3,4,5])

# def f1(x):
#     print 'call f1()'
#     return x*2
# def f2(x):
#     print 'call f2()'
#     return x*x
# def f3(x):
#     print 'call f3()'
#     return x*x*x
#
# print f1(10)


def p(x):
    return x*x
def new_fn(f):
    def fn(x):
        print 'call' + f.__name__+'()'
        return f(x)
    return fn

g1=new_fn(p)
print g1(6)