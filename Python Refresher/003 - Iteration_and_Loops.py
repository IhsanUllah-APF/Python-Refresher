#Bismillah

for ingredient in "sugar", "milk", 'tealeaves':
    print('put', ingredient, "in")

# for loop has no (). The thing that changes has been put in the variable, ingredient, and the thing that does not
# change has been put in the body of the loop, put and in. Also, "" or '' can be used for string.

for i in 1, 2, 3, 4, 5, 6, 7, 8, 9: #it would have been dificult if we had 100 numbers
    print(i)

print ("Done")

#range example
for i in range(1, 10): #the range stops one number before the last given number.
    print(i)

print("Done")

#While Loop:
# While loop is mostly used when we don't know how many times we need to iterate etc or other specific information.
# Like if, while takes condition and it keeps iterating as long as that condition is true.

n = 0.13
counter = 0

while n < 1: #Note that there are no () after while.
    counter = counter + 1
    print (n)
    n = n + 0.13
    
#Note that n is incrementing through loop though n is outside the body of loop. n is global variable so it can be
#accessed from anywhere in the program if it is not already locally available in a function.

print (n) 
#it will print the updated value of n in the global frame since the loop have changed this value as unlike function
#loop does not create its own local frame and local variable.
print (counter)
print ("Done")

#Find even numbers
for i in range(2, 10):
    if i % 2 == 0: #for odd numbers, if i % 2 == 1. Or, if i % 2 != 0. Or, if not i % 2 == 0.
        print(i)

# Use of keyword, continue.
for i in range(2, 10):
    if i % 2 == 0: 
        continue
    print(i)
    #if this condition is true, then continue will take control to for and remaining body of for loop (print) will
    #not be executed. It will quit only this iteration. In this case it will output only odd numbers.

# Use of keyword, break.
for i in range(2, 10):
    if i % 5 == 0:
        break
    print(i)
    #if this condition is true, then quit the entire loop and all the remaining iterations and get outside the body
    #of loop.

# For loop for factorial.
fac = 1
for i in range(1, 5): #range can be changed to compute factorial of other numbers. This one is for 4.
    fac = fac * i
print(fac)
    
# While loop for factorial.
fac = 1
i = 1
while i < 6:
    fac = fac * i
    i = i+1
print(fac)
  




