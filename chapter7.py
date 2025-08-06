import os

#-----------------------------------------------------
#                 FILE I/0
#-----------------------------------------------------
# open a file in read mode
#------------------------------------------------------

#f = open("demo.txt","r")

#----------------------------------------------------
# read from file
#----------------------------------------------------

# data = f.read()
# print(data)
# print(type(data))

# line1 = f.readline()   # this will give me empty space if i don't comment the above f.read() command
# print (line1)

# adds a next line

# line2 = f.readline()
# print (line2)

# line3 = f.readline()  # empty line as no data to read
# print (line3)


#------------------------------------------------
# write to a file
#------------------------------------------------

# f = open("demo.txt", "w")  #in write mode

# f.write("My name is suhani.")
# will overwrite the previous data

# f = open("demo.txt", "a")  # in append mode
# will write after the previous data in same line
# give\n for next line

# f.write ("\n I am 21 years old.")


# IF A FILE DOES NOT EXIST AND YOU TRY TO OPEN IT , PYTHON WILL ITSELF CREATE THAT FILE

# f = open("sample.txt", "w")


#----------------------------------------------------
#  Different modes of opening a file
#----------------------------------------------------
# r+ -> open for reading and writing. stream is positioned at beginning of file

# f = open("demo.txt", "r+")  
# f.write("abc")   
 
# this overwrote in starting of demo file
# reading and writing is happening through pointer
# after writing my pointer is at end of abc
# then if i read it will read after abc

# print(f.read())

#-----------------------------------------------------
# w+ -> file created it does not exist , else it is truncated. stream is positioned at beginning of file

# f = open("demo.txt", "w+") 
# print(f.read())     # file empty as truncated

# f.write("hello")


#----------------------------------------------------
# a+ -> read and append. pointer at end. no truncate

# f = open("demo.txt", "a+") 
# print(f.read())     # file empty as truncated
# f.write("hello")



#-----------------------------------------------
# with syntax
#-----------------------------------------------

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("my name is suhani")
    


#--------------------------------------------------
# delete the file
#--------------------------------------------------

# using os module

os.remove("sample.txt")



#--------------------------------------------------
# close the file
#--------------------------------------------------
# always close file at end
# not necesary in with syntax as it automatically closes file

f.close()