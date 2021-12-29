# Bismillah

pairs = [[1, 20], [2, 30], [3, 40], [4, 50]] #Nested sequences or nested lists. Also, called 2-Dimensional name.
#pairs is the name of the list. There is an outer list and in the outer list there are four inner lists. In the outer
#list, the first inner list is at index 0, the second inner list is at index 1 and so on. In the first inner list,
#1 is at index 0 and 20 is at index 1. Similarly, in the second inner list, 2 is at index 0, and 30 is at index 1.
#If we want to access a particular element, say 2 from the second inner list, then we need to type [1][0].The 1 takes
#us to index 1 in the outer list, which is the second inner list, and the 0 gets us to 2 which is located at index
# 0 in the second inner list.


print(pairs[1]) #will output the 1 index element, the second inner list, in the outer list.
print(pairs[1][0]) #will output the zeroth element (2) of index 1 element, the second inner list, of the outer list.

#put each inner list in a, and then print each inner list one by one.                 
for a in pairs: # it will ouput the elements of outer list, which are inner lists, one by one.
    print(a)

#put first element from each inner list in x, and second element in y one by one and print. The number of variables
#(x, y) must be the same to the number of values in each inner list.
for x, y in pairs:
    print("x = ", x, "and y = ", y)

pairs = [[1, 2], [2, 2], [2, 3], [4, 4], [6, 6]]
print(pairs)

same_count = 0 
# this global variable is accessible by for loop but won't be accessible by same_count = same_count+1 defined in 
#function.
for x, y in pairs:
    if x == y:
        same_count = same_count + 1

print("same_count = ", same_count)

a = [66.25, 333, 333, 1, 1234.5]
print(a)
a.append(987) #will append the value, 987, at the end of the list, a.
print(a)

a.insert(2, -1) # it will insert -1 at index 2, while existing value at index 2 will be pushed to index 3.
print(a)

print(a.index(333)) # find the value 333. When the first 333 is found, then its index is returned.

print(a)
a.remove(333) #it will remove the first 333 that it finds.
print(a)

a.reverse() 
print(a)
#it will reverse the list. The first item will go to the end, and the last element will go to start of the list.

a.sort() #it will sort the list in ascending order, starting from the smallest value in the list.
print(a)

#two ways to sort the list in the discending order.
a.sort(reverse = True) 
#this will sort the list in the descending order, starting from the largest number in list. reverse is the name of 
#the argument defined in the function sort and it is also a variable so True is assigned to it as a value which 
#means to sort the list in the descending order. reverse has default value False, which sorts the list in the 
#ascending order so it is same as a.sort().

print(a)

print(max(a)) #it will output the maximum number in the list
print(min(a)) #it will output the minimum number in the list.

#help(list) #will open help menue.

#strings are also sequences like list is a sequence but there are differences.
s = "I am a dummy string. Lorem Ipsum."

print(s[0]) #will output the zeroth element in the string, s, which is I.

print(len(s))

print(s[2:4])
#s[1] = 'x' #string does not allow assignment like this. It will output Type Error.

# help(str) #this will open string help document.

# Range is also a sequence
r = range(1, 10) # starts from 1 but stops at 9.
print(*range(1, 10)) # it outputs all the numbers in the range.
#use value at address operator(*) to print all the numbers in range. It is so maybe bcz range is a data structure.

print(*range(1, 10, 2)) 
# the last 2 is for step size. Meaning that print 1, 3, 5, 7, and 9, while leaving 1 element in between.

#Make a table of two till 2.
for j in range(1, 4): #Nested loop. First do the simple task (inner loop) and then code the outer loop.
    print("Printing table of ", j)
    for i in range(1, 3):
        print(j, " X ", i, "= ", j * i)

#List Comprehensions: list comprehension exists hardly in any other language.
nums = [1, 2, 3, 4, 5, 6, 1000]
evens = []

for i in nums:
    if i % 2 == 0:
        evens.append(i) # append that number to the list evens.

print(evens)

#A faster alternative to the above command is:
print([i    for i in nums     if i % 2 == 0]) #spaces between the three parts do not matter.
# put a number in i from the lists, nums, and check the condition if it is even, then put it in the first i and print.
# Or, we can save it in a variable, and then print it as:
evens1 = [i     for i in nums       if i % 2 == 0]#condition can be anything including calling a function, true or false.
print(evens1)

#find the factors of 12
factors = [x    for x in range(1, 12 + 1)       if 12 % x == 0] 
print(factors)
# 12 + 1 is the same as writing 13, but 12 + 1 has advantage in a sense that if we want factors of any other number,
# all we need to do is to change 12 to that number in the list comprehension.

# Tuples: Tuples and list are almost the same except that they are immutable datatype.
digits = (1, 8, 2, 8)
# enclosing the elements in [] will make digits a list, and enclosing them in () will make digits a tuple.
print(digits[1])
print(digits[1 : 3]) #for indexing still [] are used thought () are used to define tuples.
print(len(digits)) #length is a function so in case of list or tuples, () will be used.

#In short tuples and list are the same thing except that assignment cannot be done in tuples.
#digits[0] = 11 #this will output TypeError since tuple does not support assignemnt. This is the difference with list.

# tuples are immutable, meaning that once we make them, we cannot change them. The advantage of tuple is it works
# a bit faster than list. So, if we know that a sequence is not going to change, then we can make it tuple rarther
# than list.