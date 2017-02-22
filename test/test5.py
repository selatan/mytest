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


def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])


