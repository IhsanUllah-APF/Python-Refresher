#Bismillah

# () are used for function calls and tuples definition. [] are used for list and index positions. {} are used for 
# dictionaries.

d = {"package":             "A package is a module that can be added to any program",
    "random":                2,
    "unary operator":       ["Any operator that takes only one operand.", "sencond meaning"]
    }
# this has 3 comma seperated elements. Each element has two things, word and meaning. There can be many meanings for
# the same word given in the list and all written under it, but word cannot be repeated. Meaning can have any 
# datatype. 

print(d)

print(d["package"]) # it will print meaning of the word package contained in dictionary. [] do not refer to index here.
print(d["random"])
print(d["unary operator"])

# to add another word and meaning in the dictionary:
d["variable"] = "A memory location whose value can change."
# Note that in list, we cannot add an item if there is no idex position for it already. But in dictionary, since
# there are no index positions, therefore, we can add new words and meaning to it as we did above. For list, we
# have to use append, which creates a new index position and then add another element. In dictionary, we can do it
# without append.
print(d)

# Key Error: If we want to find meaning of a word that does not exist in dictionary, then we get a key error.
#print(d["python"])
# KEY = WORDS and VALUE = MEANING. A dictionary is a collection KEY-VALUE pairs.

# Iterating over a dictionary:
for k in d:
    print(k)
# it will print only keys and not values.

for k in d:
    v = d[k]
    print(k, "=", v)
# Now keys will be printed as before. For value, let us say, 'k' contains package so 'k' will be evaluated and repl-
# aced by package. Now, d[package] will be evaluated and replaced by value "A package is a module ..." as we saw 
# before and will be stored in variable, v. Then, key, package, and its value, a package is a module ..., will be 
# printed. Thus, this way both keys and values will be printed for entire dictionary through iteration. 

# To check if a particular key exists in the dictionary
print('package' in d) # can only for a key and not value. Will print True if key exists in dictionary.

if not 'else' in d:  
    print("The key, else, is not in the dictionary")
else:
    print("The key, else, is found.")
#else in d will return False if else is not in dictionary. not will make it True, and then the body of not finding
# else in d will be printed.

print(d.items())
#the function items() has been called for dictionary, d. It returns a seperate tuple for each key value pair in the
# dictionary. All the touples are enclosed in a list and the list is further enclosed in ().

l = d.items()
print(type(l))
#print(l[0])
#print(type(l[0]))
 
#for k, v in d:
#    print(k, "=", v)
# This will give ValueError. Dictionary, d, contains too many values whereas iterating variables are only 2.

for k, v in d.items():
    print(k, "= ", v)
    print(type(k))
# Now d.items() will convert dictionary, d, in tuples of key value pair. At one time, one tuple will be unpacked, its
#key will be put in k and value in v and printed. The same will be repeated for all touples including in the dictionary
# so this is the benifit of d.items(). It gives us to each touple for manipulation.

autograder_conf = {
    'url'               :           '121.52.146.108:8000',
    'username'          :           'p11111',
    'submission_pass'   :           'abc-334'        
}
print('connecting to', autograder_conf['url'], 'with username', autograder_conf['username'])
#autograder_conf['url'] will evaluate and produce the value of key, url.
#we can print or access the same information, value of url and value of username, using list as well instead of dic-
#tionary, but then we have to rememeber and tell index position which maybe difficult thing to do if we have many
#values in the list. Instead, dictionary is convinient since all we have to remember and tell the key to access value.

#dictionary use in banking for checks.
num_names = {
    1   :   'one',
    2   :   'two',
    3   :   'three',
    6   :   'six',
    20  :   'twenty',
    30  :   'thirty',
    1000:   'thousand'
}
# key is not enclosed in '' when numeric. Key can be of any immutable type such int, float, double, string, tuple, 
# but mostly string or integer is used as a key.  
print(num_names[3], num_names[1000]) # 3 is the key, and not index position.

v = 1
print(num_names[v])

#v = '1'
#print(num_names[v])
# will give KeyError since string 1 is different from integer 1, which is the key in the dictionary above.

#Datatype Casting
v = '1'
v = int(v) # v is first evaluated and replaced by string 1, then converted into integer 1 and then stored in v.
num_names[v]
print(num_names[v]) # using int(v) gives error here. So, casting has already been done seperately above.
# Now, it won't give KeyError since v contains now integer 1, which is the key in the dictionary above.












