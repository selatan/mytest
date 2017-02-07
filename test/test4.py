#!/usr/bin/python
# -*- coding: utf-8 -*-
import math



# age = 20
# if age >=18:
#     print 'your age is',age
#     print 'adult'
# print 'END'


# score =75
# if score >= 60:
#     print 'Passed'
# print 'END'

# score = 55
# if score >=60:
#     print 'passed'
# else:
#     print 'failed'

# score = 85
# if score >=90:
#     print 'excellent'
# elif score >= 80:
#     print 'good'
# elif score >= 60:
#     print 'passed'
# else:
#     print 'failed'

# L = ['Adam','Lisa','Bart']
# for n in L:
#     print n

# L = [75,92,59,68]
# sum = 0.0
# for i in L:
#     sum = sum +i
# print sum/4

# N= 10
# x =0
# while x<N:
#     print x
#     x = x +1


# #利用while循环计算100以内奇数的和
# y = 1
# sum =0
# while y<100:
#     sum = sum +y
#     print y
#     y = y+2
# print sum

# #计算1-100的整数和
# sum = 0
# x = 1
# while x <=100:
#     sum = sum +x
#     x = x +1
# print sum
#
# #计算1-100的整数和
# sum = 0
# x = 1
# while True:
#     sum = sum +x
#     x = x +1
#     if x > 100:
#         break
# print sum


# #利用while True无线循环配合break语句,计算1+2+4+8+…的前20项的和
# sum = 0
# x = 1
# while True:
#     sum = sum+x
#     x = x*2
#     if x>pow(2,19):
#         break
# print sum


# #统计及格分数的平均分
# L = [75,98,59,81,66,43,69,85]
# sum = 0.0
# n = 0
# for x in L:
#     if x < 60:
#         continue
#     sum = sum +x
#     n = n +1       #统计及格分数的个数,即循环执行了多少次
# print sum/n

# #计算1-100内奇数的和
# sum = 0
# x = 0
# while True:
#     x = x +1
#     if x >100:
#         break
#     if (x%2)==0:
#         continue
#     sum = sum + x
# print sum


# for x in ['A','B','C']:
#     for y in ['1','2','3']:
#         print (x+y)


# #使用两重循环打印出100以内所有十位数数字比个位数数字小的数
# for x in [1,2,3,4,5,6,7,8,9]:
#     for y in [0,1,2,3,4,5,6,7,8,9]:
#         if x<y:
#             print(x*10+y)



# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# print d['Adam']
# print d['Lisa']
# print d['Bart']

# d = {
#     'Adam':95,
#     'Lisa':85,
#     'Bart':59
# }
# for key in d:
#     print key +':',d[key]


# weekdays = set(['MON','TUE','WED','THU','FRI','SAT','SUN'])
# x= 'SUN'
# if x in weekdays:
#     print 'input ok'
# else:
#     print 'input error'

# #请用for循环遍历set,打印出name:score来
# s = set([('Adam',95),('Lisa',85),('Bart',59)])
# for x in s:
#     print x[0]+':',x[1]

# #给定一个set和list，对list中的每个元素，如果在set中，就将其删除，如果不在set中，就将其添加进去
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for x in L:
#     if x in s:
#         s.remove(x)
#     else:
#         s.add(x)
# print s



# print abs(-1)

# L = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in L:
#     sum = sum +i*i
# print sum

# #请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和
# def square_of_sum(L):
#     sum = 0
#     for i in L:
#         sum = sum + i*i
#     return sum
# print square_of_sum([1, 2, 3, 4, 5])
# print square_of_sum([-5, 0, 5, 15, 25])


# #从一个点移动到另一个点,给出坐标\位移和角度,计算出新的坐标
# def move(x,y,step,angle):
#     nx = x+step*math.cos(angle)
#     ny = y+step*math.sin(angle)
#     return nx,ny
# x,y = move(100,100,60,math.pi / 6)
# print x,y

#
# def fact(n):
#     if  n==1:
#         return 1
#     return n*fact(n-1)
# print fact(5)
# print fact(1)

# def power(x,n):
#     s = 1
#     while n>0:
#         s = s * x
#         n = n-1
#     return s
# print power(4,2)


# #定义一个greet()函数,它包含一个默认参数,如果没有传入,打印"Hello,world";如果传入,打印"Hello,xxx"
# def greet(name = 'world'):
#     print 'Hello,'+name+'.'
# greet()
# greet('Bart')


#计算任意个数的平均值
def average(*args):
    sum = 0.0
    if len(args)==0:
        return sum
    for x in args:
        sum = sum +x
    return sum/len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)