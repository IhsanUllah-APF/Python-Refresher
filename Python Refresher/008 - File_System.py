#Bismillah

# READING from saved files received from a client:

# Setting up absolute path.
import os
directory = 'D:\Computer Science\Programming\Data Structure\Dr.NoumanSb-Python' 
#Give the absolute path starting from drive till the last folder in which the file is actually contained.
name = 'dummy.txt'
filename = os.path.join(directory, name) # the variable directory contains absolute path.
# os.path.join() is a function and takes two arguments, the absolute path and and name of the file. Then it joins
# the absolute path with the name of the file in such a way that the forward or backslash will be adjusted itself 
# depending on the type of operating system. The absolute path combined with the name of the file is then stored in
# a variable, filename, which has been printed below.

print(filename) 
# this will print the absolute path combined with name of file,dummy.txt, through \ since I am using windows.
# still no file exists in the given directory or folder with the name of 'dummy.txt'. As per video, I have created
# the file manually, as we create files normally, and saved it in the above given directory, Dr. Nouman ..., using 
# the same name, dummy.txt. We are assuming that we will be given the file by someone else and we have saved it and
#now we want to access it and read it in python.

# Opening and reading from the file:
# The file, dummy.txt, will exist in hard disk. We will use the absolute path combined with the name of the file 
# through \, and contained in the variable 'filename', to bring the file in memory. Now, we will create a variable, 
# let's say f which is called handle, through which we will access and manipulate the file in memory.

f = open(filename, 'r')
print(f)

# open is a built in function that takes two arguments, filename which contains the path to the file and the mode, 
# such as reading or writing etc mode, in which we want to open the file.

for line in f:
    #print(line) 
    # this will create an extra line space, one through invisible new line command in the document at the end of each
    # line and the other through hidden new line command in print command.
    print(line.strip()) 
    # this command says go into line and strip it from the invisible new line command. Thus, the extra line space will
    # not appear now. Only one line space will appear because of hidden new line command in print command.

# for is intelligent enought to know that f is the file handle. So, it will get first line of the text from the file
# and put it in the variable, line, and then print it.

f.close() # Will remove all the work done in memory(RAM) when program ends to free up the space.

# A better alternative is to use a context manager to avoid problem of forgetting calling close () function.
with open(filename, 'r') as f:
    for line in f:
        print(line.strip())
print('Done')
# With is the context manager and everything indented under with is the context/body of with. Once, body of with
# is executed, and the indentation is over or we can say when we come out of the body of with, then with will itself
# automatically call the close function and do the cleaning and freeing up memory of all the things done in its body.
# We cannot call the close() function now.

# Following is the more concise way to read all the file at once rather than producing its one line at a time via
# for loop. Too big files shouldn't be read this way otherwise the entire file will be brought into memory and the
# system may crash.
with open(filename, 'r') as f:
    print(f.read()) # take the file and read it all. No need for strip() function here.
print("DoneDone")

#Convert a string into a List of strings:
split = 'a-b-c'.split('-')
print(split)
# the function, split(), will split the given string at every '-' and convert it into a list of strings where each
# element is seprated by a comma.

l = [] # this is an empty list.

with open(filename, 'r') as f:
    l = f.read().split('\n')

print(l)
# f.read() will get the entire file at once. Then, split() will look for \n and cut the content of the file at every 
# \n and convert each piece into comma seperated string element and make list of them.

# Writing to files:

out_name = 'dummy-out.txt'
out_filename = os.path.join(directory, out_name) # variable, directory, contains absolute path from above.
print(out_filename)
#file, dummy-out.txt, hasn't been created yet.

with open(out_filename, 'a') as f:
    f.write('Six ...\n')
# first, a new file will be created and stored at location given by path contained in variable, out_filename. This
# file will then be opened in memory in append mode as f, handle, for manipulation. The function, f.write(), will
# access the file through handle, f, and write in it. Write, w, mode is for overwriting. \n will insert a new line. 