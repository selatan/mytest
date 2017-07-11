# -*- coding: utf-8 -*-

#请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。

#方法一(比较啰嗦)
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def __str__(self):
#         return '(%s: %s)' % (self.name, self.score)
#
#     __repr__ = __str__
#
#     def __cmp__(self, s):
#         if self.score < s.score:
#             return 1
#         elif self.score >s.score:
#             return -1
#         else:
#             if self.name < s.name:
#                 return -1
#             if self.name > s.name:
#                 return 1
#             else:
#                 return 0
#
# L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
# print sorted(L)


#方法二
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)       #按名字升序排列
        return -cmp(self.score, s.score)        #否则按分数倒序排列

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)


#
# class Students(object):
#     def __init__(self,*args):
#         self.names = args
#     def __len__(self):
#         return len(self.names)
#
# ss = Students('Bob','Alice','Tim')
# print len(ss)




#斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
class Fib(object):

    def __init__(self, num):
        a=0
        b=1
        L=[]
        for n in range(num):
            L.append(a)
            a,b = b,a+b        #不知道啥意思
        self.num  = L
    def __str__(self):
        return str(self.num)

    def __len__(self):
        return len(self.num)

f = Fib(10)
print f
print len(f)