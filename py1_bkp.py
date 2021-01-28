#print(Module import Initiate)
#
#test='Test string'
#
#def find_index(to_search, target)
#    for i,value in enumerate(to_search)
#        if value==target
#            return i
#
#    return -1
#----------------------------lambda-------------------------------------------#
#f = lambda a,b  a+b 
#result = f(5,6)
#print(result)
#----------------------------map,filter,reduce using lambda-------------------------------------------#
#from functools import reduce
#nums=[2,3,4,5,6,7,8]
#even=list(filter(lambda n  n%2==0,nums))
#print(even)
#doubles= list(map(lambda n  n2, even))
#print(doubles)
#
#sum = reduce(lambda a,b  a+b,doubles)
#print(sum)
#----------------------------decorators-------------------------------------------#
#def div(a,b)
#    print(ab) 
#
#def smart_div(func)
#    def inner(a,b)
#        if a  b 
#            a,b=b,a 
#        return func(a,b)
#
#    return inner
#div=smart_div(div)
#div(2,4)
#----------------------------Main -$2-------------------------------------#
#def main()
#    print(manoj)
#
#if __name__=='__main__'
#    main()
#----------------------------OOPS-------------------------------------#
#class Computer
#    def config(self)
#        print(i5,16gb,1TB)
#
#comp1=Computer()
#comp1.config()
#----------------------------special method-------------------------------------#

#class Employee
#    def __init__(self,name,age)
#        self.name=name
#        self.age=age
#    def details(self)
#        print(Details are +self.name+' ,'+self.age)
#
#
#com1=Employee('Manoj','23')
#com1.details()

#----------------------------tribonacci-------------------------------------#
#q=0
#w=0
#e=1
#print(q)
#print(w)
#print(e)
#for i in range(2,100)
#    c=q+w+e
#
#    q=w
#    w=e
#    e=c
#    if c=100
#        print(c)
