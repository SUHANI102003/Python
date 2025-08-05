#-----------------------------------------------------
#                 FILE I/0
#-----------------------------------------------------

f = open("demo.txt","r")

data = f.read(5)
print(data)
print(type(data))


# always close file at end
f.close()