#INHERITANCE PROBLEMS.
#Create a class Animal as a base class and define method animal_attribute.Create another class Tiger which is inheriting Animal and access the base class method.
print("Create a class Animal as a base class and define method animal_attribute.Create another class Tiger which is inheriting Animal and access the base class method.\n")
class Animal:
    def animal_attribute(self):
        print("Animal class")
        print("Tiger runs very fast")
class Tiger(Animal):
    def animal_attribute(self):
        print("Tiger class")
        print("Here Tiger class is being inherited from Animal class \n")
        super().animal_attribute()
t=Tiger()
t.animal_attribute()
print("\n***********************************\n")



#What will be the output of the code
# print("What will be the output of the code")
# class A:
#     def f(self):
#         return self.g()
#
#     def g(self):
#         return 'A'
#
# class B(A):
#     def g(self):
#         return 'B'
#
# a=A()
# b=B()
# print(a.f(),b.f())




print("output of this code---")
print("A  B")

print("\n***********************************\n")





#Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
print("Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.\n")

class Cop:
    def add(self,name,age,work_exp,designation):
        self.name=name
        self.age=age
        self.work_exp=work_exp
        self.designation=designation

    def display(self):
        print("name--",self.name)
        print("age--",self.age)
        print("work experience--",self.work_exp)
        print("designation--",self.designation)

    def update(self):
        self.name=input("Enter name")
        self.age=int(input("Enter age"))
        self.work_exp=int(input("Enter experience"))
        self.designation=input("Enter designation")

class Mission(Cop):
    def add_mission_details(self,Mission):
        self.Mission=Mission
        print(self.Mission)

m=Mission()
m.add_mission_details("Assigned to Mission")
m.add("Khushiram",19,3,"Developer")
m.display()
m.update()
m.display()
m.add_mission_details("search")
print("\n***********************************\n")


#Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
print("Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.\n")
class Shape:
    def __init__(self,length,breadth):
        self.lentgh=length
        self.breadth=breadth

    def Area(self):
        print("Area of Square=",self.lentgh*self.lentgh)
        print("Area of Rectangle=",self.lentgh*self.breadth)


class Square(Shape):
    def sq(self):
        super().Area()

class Rectangle(Shape):
    def re(self):
        super().Area()

length=int(input("Enter the length"))
breadth=int(input("Enter the braedth"))
S=Shape(length,breadth)
S.Area()


