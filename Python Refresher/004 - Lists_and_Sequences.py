#Bismillah

digits = [1, 8, 2, 8] #example of integer list.
# this list will be save in memory location called digits. digits is name of the list. [] are used for list.
#From the [], the intepreter knows that this is list stored in variable/memory location called, digits.

print(len(digits)) # length is the built function used to find the number of items in a list.

# In Python, list starts from 0 index.
print(digits[0]) # This will output the zeroth element, 1, from the list.
#Or,
v = 0
print(digits[v]) 
#instead of 0,we can store 0 in a variable, v, and use v instead of 0. V will be evaluated and converted into 0.
print(digits[3])

print(1 in digits)
# in is binary bolean operator because it takes two operands and returns true or false. It will check if 1 exists
# in the list.
print(88 in digits)

#Example:
for i in "water", "sugar", "milk", "tea leaves":
    print("Put", i, "in")
#this program is hard coded because if we want to change ingredients, we have to make changes in the source code.

#But we can soft code as:
def make_tea(ing):
    for i in ing: 
    #it should be same name as argument in function and in for loop. In this example it is ing. for loop does not
    #create its own local frame. It operates in local frame of the function. Thus, for loop will use values stored
    #in ing present in local frame of the function. If for loop has different name than ing, then it wouldn't find
    #that different name in function local frame and will output error that that different name is undefined.
        print("put", i, "in")
ingredients = ["water", "sugar", "milk", "tea leaves", "ilachi"] #example of string list.
make_tea(ingredients) # ingredients will be evaluated and its value, the list, will be taken and passed on as 
                        #argument to the function which will be save in local variable, ing, of the called function.
# Now we don't have to make changes in source code, but any user can define its own list of ingredients and call
#the function, make_tea.

s = [1, 2, 8, 4, 6, 8, 9, 15] # example of integer lists.
#count a particular number from the list.
counter = 0
num = 8
for i in s:
    if i == num:
        counter = counter + 1

print(counter)

#Or,
#counter1 = 0 
#when variable, counter1, is defined in global frame, we get error of local unboud. Why the function does not access
#it from the global frame.
def count(seq, value): #what is the need to make a function when the same work can be done using for loop as above?
    counter1 = 0 
    # now the function access variable, counter1, since it is defined now in the local frame of the function.
    for i in seq:
        if i == value:
            counter1 = counter1 + 1
    
    return counter1
val = 15
#val = 3.3 #to check the value that does not exist in the list. The function returs 0 as it should.
v = count(s, val)
print("The number", val, "has repeated", v, "times.")
        
listtt = [1, 2, 3.3, "good", True, None]
#note that the list in python can contain different data types unlike arrays in C or C++.
print(type(listtt))
#the type of listtt is 'list' since it is a list data structure and each item in the listtt has got its own datatype.

# Modifying list.
print(listtt)
listtt[1] = 55
print(listtt)

listtt[2] = "a"
print(listtt)
#same way elements in the list can be replaced element of any other datatype including string, float, True, None etc.

#return particular elements from the list:

print(listtt[0 : 2]) 
# 0 and 2 are the index positions in the list and will return the values at index positions 0 and 1. It will start
# from left of 0 and stop at left of 2.

print(listtt[1:]) # will output all the values starting from left of index 1 and go till the end of the list.

print(listtt[:]) #produce the complete list. print(listtt) will also produce the complete list.

print(listtt[-1]) #will output the first number from the last/end. None is at index 5 as well as at index -1.

print(listtt[-4 : -1]) #will output all the elements starting from left of -4 index to the left of -1 index.

print(listtt[:3]) # start from left of 0 index and strops at left of index 3.

