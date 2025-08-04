#--------------------------------------------------
#               CONDITIONAL STATEMENTS
#--------------------------------------------------
"""
light = input("light color :")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#-----------------------------------------------------

marks = int(input("marks :"))

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

#-------------------------------------------------------

# ternary operator
food = input("food :")
eat = "YES" if food == "cake" else "NO"
print (eat)



#--------------------------------------------------
#                    STRINGS
#--------------------------------------------------
str1 = "This is a string \n hello"
print(str1)

str2 = 'Suhani jain'


#concatenation
print(str2+str3)


#-----------------------------------------
#length of a string
#-----------------------------------------
print(len(str2))

final_string = str2 + " " + str2
print(final_string)
print(len(final_string)) # will count space too


#------------------------------------------
# Indexing
#-----------------------------------------
ch = str2[4]
print(ch)

# str2[4] = "r"
# print(str2)   #error -'str' object does not support item assignment

#--------------------------------------------
# Slicing
#--------------------------------------------

slice = str1[1:4] # 4 not included
print(slice)       # his
print(str1[5:len(str1)])
print(str1[1:])
print(str1[:7])
print(str2[-4:-2]) #negative slicing

#--------------------------------------------
# string functions
#--------------------------------------------

str = "i am studying python"

print(str.endswith("on"))
print(str.endswith("py"))

print(str.capitalize())  # first letter capital
print(str)  
#does not change original string
# but if we want to do this >

# str = str.capitalize()
# print(str)

print(str.replace("o", "a"))

print(str.find("am")) # returns the 1st index

print(str.count("am"))  # 1 as am exists 1 time in str

"""
