# # #Create a circle class and initialize it with radius.Make two methods getArea and getCircumference inside this class.
print("Create a circle class and initialize it with radius.Make two methods getArea and getCircumference inside this class.\n")
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of circle is=",3.14*self.radius*self.radius)
    def getCircumference(self):
        print("\nCircumference of circle is=",2*3.14*self.radius)
radius=int(input("Enter the radius"))
obj=Circle(radius)
obj.getArea()
obj.getCircumference()
print("\n*************************************\n")



'''Create a student class and initialize it with name and roll number.Make methods to:
1.Display-it should display all informations of the student
'''
# print("Create a student class and initialize it with name and roll number.Make methods to:\n1.Display-it should display all informations of the student\n")
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def Display(self):
        print("The name of student is--",self.name)
        print("Roll number is--",self.rollno)
name=input("Enter the name of student")
rollno=int(input("Enter the rollno of student"))
obj1=Student(name,rollno)
obj1.Display()
print("\n*************************************\n")



'''
Create a Temperature class.Make two methods:
1.convertFahrenheit-it will take celcius and will print it into Fahrenheit.
2.convertCelcius-it will take Fahrenheit and will convert into Celcius.
'''
# print("Create a Temperature class.Make two methods:\n1.convertFahrenheit-it will take celcius and will print it into Fahrenheit.\n2.convertCelcius-it will take Fahrenheit and will convert into Celcius.\n")
class Temperature:
    def convert_Fahrenheit(self):
        c_temp=int(input("Enter the temperature in Celcius"))
        print(c_temp,"C")
        print("Temperature in Fahrenheit=",(c_temp*1.8)+32,"F")
    def convert_Celcius(self):
        f_temp=int(input("Enter the temperature in Fahrenheit"))
        print(f_temp,"F")
        print("Temperature in Celcius=",(f_temp-32)/1.8,"C")

obj=Temperature()
obj.convert_Fahrenheit()
obj.convert_Celcius()
print("\n*************************************\n")



'''
Create a class MovieDetails and initialize it with Movie name,artistname,Year of release and ratings.Make methods to
1. Display-Display the details:
2. Update-Update the movie details.
'''
print("Create a class MovieDetails and initialize it with Movie name,artistname,Year of release and ratings.Make methods to\n1. Display-Display the details:\n2. Update-Update the movie details.\n")
class MovieDetails:
    def __init__(self,Movie_name,Artist_name,YoR,Ratings):
        self.Movie_name=Movie_name
        self.Artist_name=Artist_name
        self.YoR=YoR
        self.Ratings=Ratings
    def Display(self):
        print("Movie_name--",self.Movie_name)
        print("Artist_name--",self.Artist_name)
        print("Year of releasing--",self.YoR)
        print("Ratings--",self.Ratings)
    def Update(self):
        self.Movie_name=input("Enter the name of Movie")
        self.Artist_name=input("Enter the name of Artist name")
        self.YOR=int(input("Enter the year of Releasing"))
        self.Ratings=float(input("Enter the Ratings"))
Movie_name=input("Enter the name of Movie")
Artist_name=input("Enter the name of Artist name")
YoR=int(input("Enter the year of Releasing"))
Ratings=float(input("Enter the Ratings"))
obj=MovieDetails(Movie_name,Artist_name,YoR,Ratings)
obj.Display()
obj.Update()
obj.Display()
print("\n*************************************\n")



'''
Create a class Expenditure and initialize it with expenditure,saving.Make the following methods.
1.Display expenditure and savings.
2.Calculate total salary.
3.Display salary.
'''
print("Create a class Expenditure and initialize it with expenditure,saving.Make the following methods.\n1.Display expenditure and savings.\n2.Calculate total salary.\n3.Display salary.")
class Expenditure:
    def __init__(self,exp,save):
        self.exp=exp
        self.save=save
        print("Expenditure=",self.exp)
        print("Saving=",self.save)
    def total_salary(self):
        t=self.exp+self.save
        return t
    def Display(self,s):
        self.s=s
        print("Total salary is=",self.s)
exp=int(input("Enter the Expenditure"))
save=int(input("Enter your saving"))
obj=Expenditure(exp,save)
a=obj.total_salary()
obj.Display(a)
