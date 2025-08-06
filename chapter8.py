#-------------------------------------------------------
#              OBJECT ORIENTED PROGRAMMING
#-------------------------------------------------------


# class student:
#     name = "karan kumar"

# alone class does nothing
# we have to create a object first
# imagine it as an empty class with no students inside

# our object = student
# so when we create object, we are adding student to our class

# s1 = student()  # object or instance of class
# print(s1)
# print(s1.name)  # name for student 1

# s2 = student()
# print(s2.name)  # same name as karan


# class car :
#     color = "blue"
#     brand = "toyota"

# car1 = car()
# print(car1.color)
# print(car1.brand)


#---------------------------------------------------
#    CONSTRUCTOR  - init function
#---------------------------------------------------
"""
# class car :
#     color = "blue"
#     brand = "toyota"

# car1 = car()  # automatic constructor excecuted, we do not see init function
# print(car1.color)
# print(car1.brand)


# data stored inside class is called attributes

class student:
     
     clg_name = "thapar" # class attributes i.e, same/shared by all class objects/instances
    # stored only once in memory

     # default constructor
     def __init__(self): 
          pass
          
      # parameterized constructor
     def __init__(self, name, marks):  
          print(self)  # self == s1
          self.name = name   # instance/object attributes i.e, different for every object, stored many times in memory depending on no. of objects
          self.marks = marks
          print("adding new student in database")


s1 = student("karan", 78) 
# print(s1)  
print(s1.name, s1.marks)   

s2 = student("arjun", 90)
print(s2.name, s2.marks, s2.clg_name)
print(student.clg_name) # also valid as clg_name is a class attribute
#print(student.name)  # error as name is obj attribute
"""

# class student:
     
#      clg_name = "thapar"
#      name = "anonymous" # class attr

#      def __init__(self, name, marks):  
#           self.name = name   
#           self.marks = marks
#           print("adding new student in database")

# # now i have 2 names-- one is a class attribute & another a obj attribute
# # which one will run?

# s1 = student("karan", 97)
# print(s1.name)  # karan ; as obj attr > class attr

#---------------------------------------------------
#    METHODS (functions that belong to objects)
#---------------------------------------------------
# class student:
#      clg_name = "thapar"

#      def __init__(self, name, marks):  
#           self.name = name   
#           self.marks = marks
#           print("adding new student in database")

#      def welcome(self):
#           print("welcome student", self.name)

#      def get_marks(self):
#           return self.marks

# s1 = student("karan", 97)
# s1.welcome()  # always add self 
# print(s1.get_marks())


#---------------------------------------------------
#    STATIC METHODS 
#---------------------------------------------------

class student:

  def __init__(self, name , marks):
    self.name = name
    self.marks = marks 
    
  # def hello():  
  #   print("hello")

  @staticmethod       # decorator
  def hello():  
    print("hello")

  def avg(self):
   sum = 0
   for value in self.marks:
     sum += value
   print ("hi", self.name, "your avg score is:", sum/3)

s1 = student("rishi", [78,98,89])
s1.avg()
#s1.hello() # will give error as no self defined
# but this function has no use of self -> so declare it as static

s1.hello()


