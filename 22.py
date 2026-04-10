# constructor

class Student:


    def __init__(self,name):
        print("Inside Constructor")
        self.name= name
        print("All variables initialized")


    #instance method
    def show(self):
        print("Hello , my name is", self.name)


#creat object using constructor
s1 = Student('Emma')
s1.show()

# non parametrized constructor

class Company:

    #no argument consructor
    def __init__(self):
        self.name= "Pynative"
        self.address = "ABC Street"


    # a method for printing data members
    def show(self):
        print("Name", self.name,"Address", self.address)



#creating object of the class
cmp = Company()
#calling the instance method using the object
cmp.show()


#parametrized constructor

class Employee:
    # parametrized constructor
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    #display object
    def show(self):
        print(self.name,self.age, self.salary)

#creating object of the Employee class
emma = Employee("Emma",23,7800)
emma.show()

kelly = Employee("kelly",32,8700)
kelly.show()


#Constructor with deafult values

class Student:

    #constructor with default values age and classroom
    def __init__(self,name,age=12,classroom= 7):
        self.name =  name
        self.age = age
        self.classroom =classroom

    # display students
    def show(self):
        print(self.name, self.age, self.classroom)

#creating object of the student class
emma = Student("Emma")
emma.show()

kelly = Student("kelly",13)
kelly.show()



#Konstruktor yordamida  classning obyektlarini sanash

class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1

# creating objects
e1 = Employee()    #reference count
e2 = Employee()
e3 = Employee()
print ("The number of Employee:", Employee.count)

# konstructor = yaratishda ishlatilsa
#destruktor = ochiirishda ishlatiladi

# destructor  -- del()

class Student:

    #constructor
    def __init__(self,name):
        print("Inside Constructor")
        self.name = name
        print("Object initialized")


    def show(self):
        print("Hello , my name is", self.name)


    #destructor
    def __del__(self):
        print("Inside destructor")
        print("Object destroyed")


# create object
s1 = Student('Emma')
s1.show()

#delete object
del s1


#Vorisdorlik va polimorfizm

class Odam:
    qollar_soni = 2
    oyoqlar_soni = 2


class Jangchi(Odam):   #Odam dan vorisdorlik oldi
    energiya = 100
    jang_qiyinligi = 30 # bitta jang qilsa qancha energiya yoqotadi

    def jang_qil(self):
        if self.energiya >= self.jang_qiyinligi:
            self.energiya -= self.jang_qiyinligi
            print(f"Jangda {self.jang_qiyinligi} energiya yoqotildi, {self.energiya} qoldi")
        else :
            print("Jang uchun energiya yetarli emas!!!")

Botir  = Jangchi()
Botir.jang_qil()
Botir.jang_qil()
Botir.jang_qil()
Botir.jang_qil()
print(Botir.qollar_soni)



#

class Shifokor(Odam):
    dorilar = ['Trimol',"suv"]


    def davola(self):
        if len(self.dorilar)>0:
            dori = self.dorilar.pop()
            print(f'{dori} yordamida davolandi')
        else:
            print("dori qomadi")

Doniyor = Shifokor()
Doniyor.davola()
Doniyor.davola()
Doniyor.davola()
Doniyor.davola()


#
class JangchiShifokor(Jangchi,Shifokor):
    pass

superman = JangchiShifokor()
superman.davola()
superman.jang_qil()

#
class Person:
    origin_country = "USA"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,words):
        print(f"{self.name} speaks:{words}")



class Employee(Person):
    def __init__(self,name,age,gender,salary,job_title):
        super().__init__(name,age,gender)
        self.salary= salary
        self.job_title = job_title


    def display_info(self):
        print(f"Employee {self.name}  works a {self.job_title}")



# Diamond problem and Resolution Method Order

class Base:
    def call(self):
        print("Base class")

class Left(Base):
    def call(self):
        print("Left class")

class Right(Base):
    def call(self):
        print("Right class")

class Child(Left,Right):
    pass

child = Child()
child.call()
print(Child.mro())  #mro sini chiqaradi


#polymorphizm
#polymorphism Build in function  len()
students = ['Emma', "Jessa","Kelly"]
school = "ABC School"

#calculate count
print(len(students))
print(len(school))















