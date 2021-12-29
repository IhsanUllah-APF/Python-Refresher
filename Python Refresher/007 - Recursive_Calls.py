#Bismillah

#use of not
def absolute_value(x):
    if not x < 0:
    #suppose x = 5. First, x < 0 is evaluated. Here, it is evaluated to be false. 'not' will convert false into 
    # true, so if will get true, which means body of 'if' will be executed. 
        return x
    
    else:
        return -x

print(absolute_value(5))
print(absolute_value(-3))

#nested if
a = 6
b = 8

if a > 5: #Note that there are no () around condition in if.
    if b > 6:
        print("a is greater than 5 and b is greater than 6")
    
    else:
        print("a is greater than 5 but b is not greater than 6")

else: #there could be own if-else block in else as well.
    print("a is not greater than 5")

print("Done")

#example: square root

def sqrt(x, guess = 0): #guess = 0 is the default value.

    if x < 0: 
        return None
    #Note that there are two ifs and one else. The can be multiple ifs or elifs before else. Even else can be 
    # option in some situations. 

    if good_enough(guess, x): 
    #guess and x will be evaluated and then their values will be used as arguments when calling function,
    #good_enough.
        return guess
    
    else:
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)

def good_enough(guess, x):
    if abs(guess * guess - x) < 0.1:
        return True 
    
    else:
        return False 

def improve_guess(guess, x):
    if guess < x:
        return guess + 0.1

    else:
        return guess - 0.1

print(sqrt(4, 1.8))