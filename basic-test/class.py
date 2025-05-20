#create class use class

class myclass:
    x=5

#object =p1

p1 = myclass()
print(p1.x)

#alled automatically every time
#  the class is being used to create a new object.
#self = parameter itself
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p2 = person("john", 36)
print(p2.name)
print(p2.age)

#The __str__() function controls what should be
#returned when the class object is represented as a string.

def _str_(self):
    return f"{self.name}({self.age})"

print(p2)

#method in object()

class human:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def mymethod(self):
        print("hello my name is" + self.n)

h1 = human("anna", 23)
h1.mymethod()

#self parameter same like this in java 

class people:
    def __init__(myobj,nama,umur):
        myobj.nama= nama
        myobj.umur = umur

    def mymethod2(abc):
        print("hello my id is" + abc.nama)

pl1 = people("bola", 7)
pl1.mymethod2()

#delete obj

del pl1.umur


class student:

    count =0   #class var
    total_gpa=0

    def __init__(self,nm,gpa):  #constructor method
        self.nm =nm
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa 

    def get_info(self):     #instance method
        return f"{self.nm} {self.gpa}"
    
    @classmethod
    def get_count(cls):    #class method use cls parameter
        return f"Total of students: {cls.count}" # can access class var
    
    @classmethod
    def get_avggpa(cls):
        if cls.count ==0:
            return 0
        else:
            return f"{cls.total_gpa/ cls.count:.2f}"
    
print(student.get_count())

s1 = student("spngbob", 2.0)
s2 = student("patrick", 3.0)
s3 = student("sandy", 4.0)

print(s1.get_info()) #call instance method
print(s2.get_info())
print(s3.get_info())

print(student.get_count()) #call class method
        
print(student.get_avggpa())

class robot:  #no contructor case
     def introduceSelf(self):
        print("robot name is " +self.namer)

r1 = robot()        #create obj
r1.namer = "tom"
r1.color = "red"
r1.weight = 30

r2 = robot()
r2.namer = "jery"
r2.color = "blue"
r2.weight = 40

r1.introduceSelf()
r2.introduceSelf()

class robot2:
     def __init__(self, gname, gcolor,gweight): #constructor
         self.gname = gname
         self.gcolor = gcolor
         self.gweight = gweight

     def intro(self):
        print("robot name is " +self.gname)


r3 = robot2("tom", "red", 80)     #create obj w constructor
r4 = robot2("jerry", "blue", 30)

r3.intro()
r4.intro()


class saram:
    def __init__(self, sname, swork, sissitting):
        self.sname = sname
        self.swork = swork
        self.sissitting = sissitting

    def sit_down(self):
        self.sissitting = True

    def stand_up(self):
        self.sissitting = False

ss1 = saram ("edward", "vampire", False)
ss2 = saram("swan", "police", True)

#ss1 owns r1
ss1.robot2_owned = r3
ss2.robot2_owned = r4

ss1.robot2_owned.intro()
ss2.robot2_owned.intro()


  
