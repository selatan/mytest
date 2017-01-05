# -*- coding: utf-8 -*- 

#__init__方法 使用实例  
class Person():
    def __init__(self,name):
        self.name=name
    def sayhi(self):
        print("Hello,my name is.%s"%(self.name))


p=Person("Swaroop")
p.sayHi()




# def sayHi(self,name): 
# print "Hello, my name is, %s"%(name)  
# p = Person() p.sayHi("hehe")      


def sayHi(self,name):
    print "Hello,my name is,%s"%s(name)






#占位符输出
 num=10
 print "a=%d,b=%o,c=%x" %(num,num,num)


     class NumberCounter(): 
    number=0 # #
    def __init__(self): 
       NumberCounter.number += 1

# m1=NumberCounter()
 # print NumberCounter.number
 # m1.__init__() # print NumberCounter.number



#     class A(): 
#     def __init__(self):
 #         print "一个实例输出" # a=A() # a.__init__()


#    class B(): 
#  def t(self): 
#  print "一个实例输出" b=B() b.t() 