#-------------------------------------------------------
#                  DICTIONARY AND SET
#-------------------------------------------------------
"""
info = {
    "key" : "value",
    "name" : "suhani",
    "age" : 23,
    "marks" : 87.6,
    "is_adult" : True,
    "subjects" : ["python", "math", "C"],
    "topics" : ("dict", "set")
}

print(info)
print(type(info))
print(info["name"])
print(info["topics"])

# null dict
null_dict = {}
print(null_dict)
null_dict["name"] = "suhani"

info["name"] = "atul"   # overwrite
info["surname"] = "jain"  #added another key value pair
print(info)


# nested dictionary

student = {
    "name" : "suhani",
    "subjecs" : {
        "phy" : 78,
        "math": 98,
        "eng" : 87
    }
}

print(student["subjecs"]["math"])


#-------------------------------------------------------
#                  DICTIONARY METHODS
#-------------------------------------------------------
print(student.keys())  # list format # no nested keys

print(list(student.keys())) 

print(len(list(student.keys())))


print((student.values())) 


print(list(student.items())) 


print(student.get("name2"))  # no error -> None
# print(student["name2"])   #error  


new_dict = {"city" : "delhi", "age" : 16}
student.update(new_dict)
print(student)

"""
#-------------------------------------------------------
#                        SETS
#-------------------------------------------------------

collection = {1,2,3,4, "hello", "world"}
sets = {1,2,2,3} #  cannot repeat -> {1,2,3}

print(sets)
print(len(sets))
print(collection)
print(len(collection))
print(type(collection))


# null set
#set1 = {}  # empty dict

set1 = set()
print(type(set1))


#-------------------------------------------------------
#                     SETS METHODS
#-------------------------------------------------------

set1.add(1)
set1.add(2)
set1.add(6)
set1.add("name")
set1.add((1,2,3))  #tuple
# set1.add([3,4,5])  # error as list cannot be added

set1.remove(2)
print(set1)
print(len(set1))

# set1.clear()
# print(len(set1))  # 0

set2 = {"hello", "i am", "coding", "in", "python", 6, 1}
print(set2.pop())  # random pop


print(set2.union(set1)) 
print(set2.intersection(set1))
