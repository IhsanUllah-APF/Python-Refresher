#Bismillah

def square(x): 
#definition of function, square, which takes 1 formal parameter/input, whose type python will determine itself. 
# Ends with :
    return x * x  #indent is must to indicate body of a function. 
    #body of function. take value of x and multiply it with itself and return it. Left intended.
    #def and return are keywords.

a = (square(5)) #function call with argument or actual parameter.
print(a)

b = type(a) #call to function, type, to find out type of variable, a, and store it in variable, b.
print(b)

c = (square(5.0)) #function call with argument or actual parameter.
print(c)

d = type(c) #call to function, type, to find out type of variable, c, and store it in variable, d.
print(d)

def sum_squares(x, y): #definition of function, sum_squares, which takes two parameters.
    return square(x) + square(y) #return statement can include function calls.

print(sum_squares(3, 4)) #function print can include a function call.

# Invalid operation of multiplying string with int will result into Type Error.

# sum_squares('a', 3) 

