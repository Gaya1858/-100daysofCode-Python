'''
OOP -Object oriented programming
class name always starts with capital letter
class is blueprint of an object
object's behavior called methods (like, student- studying sleeing and eatting)
object has some attributes (like student has rool no, name and height)

variables
instance variable - it will be different for each object we create - object level
static variable - class level - when the object's name or something is same for  all the object that we create
local variable - we create inside the method and it is method level
reference variable - to create object of a class. we use this variable to access the objects methods and instance variables.\

methods
instance methods: if we use atleast one instance variable then the method is called instance method
class methods: can have at least one static variable or local variable but not instance variable
static methods: no instance variable or static variables involved - just local variables used

decorator - @classmethod keyword is used for static variable accessibility. without the keyword it will think of
            instance variable or through error . PVM will create a class level objects automallically when it sees the
            static variables. we should add the  decorator to let know the JVM
decorator - @staticmethod keyword is used when the method has only local variables to use.it is optional

constructor - method that starts with def --init--(self)
            it will be created automatically by the python VM once the object is created.
'''

class Student:
    college_name ="MSU"
    college_dept ="Computer Science"
    def __init__(self,name,rolllno,age):
        self.name =name
        self.rollno =rolllno
        self.age = age

    def show(self):
        print("Student Name: ",self.name)
        print("Roll No: ",self.rollno)
        print("Age: ",self.age)
    @staticmethod
    def add(a,b,c):
        return a+b+c
    @classmethod
    def static_use(cls):
        print("College Name: ",cls.college_name)
        print("Depatment: ",cls.college_dept)

''' student1,student2 and student3 are reference variables. 
Using these refence we can access the methods and variables inside thhe class.'''

student1 = Student("Laya","100","2")
student2 = Student("Rithu","101","5")
student3 = Student("Kanishka","102","8")

student1.static_use()
student1.show()
student2.show()
student3.show()
