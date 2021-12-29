#Bismillah

#scope or lexical scope refers to the places from where a function/variable can be seen and accessed.
def f(x): # this x is the formal parameter. It's scope should also be limited/local to this function.
    y = 1 #this y is local variable, it's scope is limited only to this function.
    x = x + y #this will add value in local x and in local y and then store sum in the local x.  
    print("x = ", x) #this will print local x.
    print("p = ", p) #variable, p, will not be created in local frame of this function.
    return x #this will return local x and the local frame of function will vanish.


p = 20 #declared/defined after definition of function, f(x), in whose body p has been used. This is global variable.
x = 3 #this x is global variable.
y = 2 #this y is global variable.
z = f(x) #value of x = 3 used as actual parameter. Return value from the function will be stored in variable, z.
#p, x, y variables will be constructed in global frame and corresponding values will be stored in them. Z will also
#be made in global frame and return value from the function will be stored in it.

print("z = ", z) #will print the value contained in global z.
print("x = ", x) #will print the value contained in global x.
print("y = ", y) #will print the value contained in global y.
#print function has () and strings are written in "" and , and variable name are also written.

#Next example
k = 25 #global variable. Also, declaration of a variable cannot be done without assignment in Python.

def f1(x1):
    k = 1
    print("k = ", k) 
    #will produce 'unbound local error' as it is trying to read and print local, k, but it has not been executed yet.
    x = 25 + 9

    #k = 1 
    #this k is local variable. Put this instruction before print to avoid the error. The solution is to define this
    # variable, k, before print command above.

x1 = 2
f1(x1)

#Next example - absolute value
def absolute_value(x): 
#this function is an example of compound statement due to having multiple instructions in it's body. 
    """Computes absolute value """ #document string which tells others what does this function do?
    if x > 0: #condition is right-indented and terminates with :
    #will return bolean value (true/false). This is conditional expression. If true, then body of if will be executed
    #This whole if-else structure allows program to work in branches and make decisions depending on which condition
    #is true.
        return x 
        #body of if is further right-indented. One indent to get into body of function and another needed to get in
        #body of if.
    
    elif x == 0: #elif also ends with : There could be multiple elif. elif shouldn't be written before if.
        return 0
    
    else: #if, elif and else all have been combined and all ending with : No need to write condition with else.
        return -x 

print(absolute_value(5)) #the value returned from function call, absolute_value(5), will be printed.
print(absolute_value(0))
print(absolute_value(-5))