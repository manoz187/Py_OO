#----------------------------imports-------------------------------------------#
#from py1 import find_index,test 
#import sys
#from random import randrange
#from calendar import isleap
#import os

#courses =['math','compsci','physics']

#random_number=randrange(9)

#print(random_number)
#print(random_course)

#print(os.__file__)
#index = find_index(courses,random_course)
#print(index)
#print(test)
#leap=isleap(2020)
#print(leap)



#----------------------------class-------------------------------------------#
#class Employee:
#    def __init__(self,first,last,dob):
#        self.first=first
#        self.last=last
#        self.dob=dob
#        self.email=first+last+dob+"@gmail.com"
#    def fullname(self):
#        return '{} {}'.format(self.first,self.last)
#        
#emp_1=Employee('manoj','kumar','1871997')
#
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
#----------------------------main-------------------------------------------#
#import py1
#print('Manu')
#----------------------------types of methods------------------------------------------#

#class Student:
#    school="SCTS"
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#    
#    def avg(self):
#        print((self.m1+self.m2+self.m3)/3)
#
#    @classmethod
#    def info(cls):
#       print(cls.school)
#
#    @staticmethod
#    def info1():
#        print("This is CNN")
#
#s1=Student(12,13,14)
#s1.avg()
#Student.info()
#Student.info1()
#----------------------------Inner functions------------------------------------------#

#class Employee:
#
#    def __init__(self,name,salary):
#        self.name=name
#        self.salary=salary
#        self.comp = self.Company()
#    
#    def show(self):
#        print("name is "+self.name)
#        print("salary is "+self.salary)
#        self.comp.show()
#
#    class Company:
#        def __init__(self):
#            self.name='MS'
#            self.city='NY'
#        def show(self):
#            print(self.name,self.city)
#
#emp1=Employee('Manoj','3L')
#
#com1=emp1.show()

#sys.setrecursionlimit(15000)
#def fib(n):
#    
#    if n==0:
#        return 0
#    elif n==1:
#        return 1
#    else:
#        return fib(n-1)+fib(n-2)
#
#print(fib(9))



