'''#ASSIGNMENT - CLASSES AND OBJECTS
#question-1 (Area And Circumference)
class circle:
    def __init__(self, rad):
        self.radius = rad
    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
rad=int(input("enter radius of circle :"))
c=circle(rad)
print("area is ",c.getArea())
print("circumference is ",c.getCircumference())


#question-2 (Student info.)
class student:
    def __init__(self):
        self.name=(input("enter your name :"))
        self.roll=int(input("enter rollno :"))
    def setAge(self):
        self.age=int(input("enter your age :"))
    def setMarks(self):
        self.marks=int(input("enter the  marks :"))
    def display(self):
        print("name:",self.name,"\n","roll-no:",self.roll,"\n","age:",self.age,"\n","marks:",self.marks)
s=student()
s.setAge()
s.setMarks()
s.display()


#question-3 (Temperature)
class temp:
    def convertFahrenheit(self):
        self.c=int(input("enter temperature in celsius :"))
        return((9/5)*self.c+32)
    def convertCelsius(self):
        self.f=int(input("enter temperature in Fahrenheit :"))
        return(((self.f-32)*5)/9)
t=temp()
print(t.convertFahrenheit())
print(t.convertCelsius())



#question-4
class Movie:
    def __init__(self):
        self.artistname = input("enter artist name :")
        self.year=input("enter year :")
        self.rating=int(input("enter ratings out of 10 :"))
    def add(self):
        self.moviename=input("enter the movie name :")
        self.collection=int(input("enter total collection :"))
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.year)
        print(self.rating)
        print(self.collection)
m=Movie()
m.add()
m.display()




#question-5 (class)
class animal:
    def animal_attribute(self):
        return("print tiger.")
class tiger(animal):
    pass
t=tiger()
print(t.animal_attribute())


#question-6 
output will be:
A B
A B
'''

#question-7 (area)
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return(self.length*self.breadth)
class rectangle(shape):
    pass
class square(shape):
    pass
l=int(input("enter length :"))
b=int(input("enter breadth :"))
r=rectangle(l,b)
s=square(l,b)
print("area of rectangle ",r.area())
print("area of square ",s.area())

