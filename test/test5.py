#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

# f=abs
# print f(-20)

# def add(x,y,f):
#     return f(x)+f(y)
# print add(-3,-9,abs)
# print add(25,9,math.sqrt)


# def f(x):
#     return x*x
# print map(f,[1,2,3,4,5,6,7,8,9])

#假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，
#把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list
# def f(L):
#        return L[0].upper()+L[1:].lower()
# print  map(f,['adam', 'LISA', 'barT'])


# #请利用reduce()来求积
# def prod(x, y):
#     return x*y
# print reduce(prod, [2, 4, 5, 7, 12])

# #取出一个list中的奇数
# def is_odd(x):
#     if x%2==1:
#        return x
# print filter(is_odd,[1,4,6,7,9,12,17])

# #利用filter()过滤出1~100中平方根是整数的数,即结果应该是:[1,4,9,16,25,36,49,64,81,100]
# def is_sqr(x):
#     r = int(math.sqrt(x))        #取出x的平方根的整数
#     return r*r== x               #返回这个整数的平方!!!
# print filter(is_sqr,range(1, 101))         #整数的平方的范围是1~101,不包含101


# def t(s1,s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     return u1,u2
# print t('bob','about')


#对字符串排序时,有时候忽略大小写排序更符合习惯.请利用sorted()高阶函数,实现忽略大小写排序的算法.
#分析:对于比较函数cmp_ignore_case(s1,s2),要忽略大小写比较,就是先把两个字符串都变成大写(或者都变成小写),再比较
def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 >u2:
        return 1
    if u1<u2:
        return -1
    return 0
print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)

