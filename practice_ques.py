
#--------------------------------------------------
# WAP to check if a list is palindrome or not
#--------------------------------------------------

list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1): 
    print("PALINDROME")
else :
    print("NOT A PALINDROME")