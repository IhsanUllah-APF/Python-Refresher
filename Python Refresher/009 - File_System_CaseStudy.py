# Bismillah

# Access and manipulate already stored file.
import os
directory = 'D:\Computer Science\Programming\Data Structure\Dr.NoumanSb-Python' # absolute path
name = 'datafile.csv'

csv_filename =  os.path.join(directory, name) # variable, csv_filename, will contain a path to the file, datafile.csv
print(csv_filename)

with open(csv_filename, 'r') as f:
    for line in f:
        print(line.strip().split(','))

# running loop to read each row seperately since each row in a file contains data about a seperate student. We could
# have though read the entire file at once throug f.read() if desirable. strip() will remove any empty spaces by 
# removing \n etc. split(',') will cut the content wherever it sees comma and return lists of strings in which each
# row is a seperate string. f.read() will perhaps make one list of strings since it reads entire file at a same time,
# whereas for only takes one row in variable, line, at a time and then strip, split and print it in form of a list.
# So, using for loop, we get multiple lists of string, one list for each row.
# Split() has deleted the commas contained in the file. The commas that we see in the lists now are the commas used
# in a list to seperate elements in a list from each other. 

# Make a list (outer list) which further contains inner lists as elements. Each inner list should be a seperate row
# in a file.
rows = [] # an empty list.
with open(csv_filename, 'r') as f:
    for line in f:
        print(line.strip().split(','))
        rows.append(line.strip().split(','))
print(rows)
# rows now contain an outer list which further contains inner lists of strings, one inner list for each row in file.
# So, the total number of elements (inner lists) in the outer list will be equal to the number of rows in the file.
# and each inner list (element of outer list) will contain number of elements equal to the number of columns in each
# row in a file.

# convert the strings in each inner list into floats for a desirable operation.
for r in rows[1:]: # take the first element, which is inner list itself, in the outer list and put it in variable, r.
    for i in range(2, 6):
        r[i]= float(r[i]) 

# r contains the first element in the outer list, which is the second inner list. r[2] gives value present at second
# index in that inner list and convert in into float from string and store it at the same place, at second index in
# the same second inner list.
print(rows)
# Now all the numbers have been converted from string into floats. We can conduct any meaningful and desirable oper-
# ation on them and save them in a seperate file as well. The word we do on the floats now maybe required in a Data
# Science project.

# Writing CSV files.
j = ','.join(['a', 'b', 'c']) # take a list of strings and join each string element through comma and return string.
print(j)                      # In short, split makes a list from a string and join makes a string from list.
print(type(j)) # j is a string.
# the list, rows, can be converted into string using join.
# the list, rows, before joining:
print(rows)
# before joining, convert the float values in inner lists of outer list row into strings as join requires:
for r in rows[1:]:
    for i in range(2, 6):
        r[i] = str(r[i])
print(rows)

# or the above can be done through list comprehension as:
for r in rows: # for knows that rows is a list, so it will take one element at a time and put it in a variable, r.
    lc = [str(c)    for c in r] # this for takes each element in r and put it in c and then convert it in string.
print(lc)

out_rows = []
for r in rows: # takes an element, inner list, and put it in variable, r.
    r = [str(c)     for c in r] # take each element from r, put it c, convert it in string and save it in same r.
    out_rows.append(r) # append the entire row contained in r to the list, out_rows.

print(out_rows)
print('Done')

# Since the list, out_rows, contains no floats now. Rather, it contains an outer list which further contains inner
# lists and each inner list contains all strings now as required by join.
for r in out_rows:
    out_line = ','.join(r)
    print(out_line)
print(type(out_line))
# The list which contained outer list which further contained inner list and each inner list was a combination of
# strings and floats. Now the entire outer list and inner lists (or list of lists ) have been converted into string 
# or comma seperated values, csv. Let us say, we want to save these comma seperated values in a new file.

# directory same as above.
name_csvout = 'datafile-out.csv' 
csv_filename_out = os.path.join(directory, name_csvout)

with open(csv_filename_out, 'w') as f:
    for r in out_rows:
        out_line = ','.join(r)
        f.write(out_line +'\n') #f.write() does not insert a new line itself.

# since the mode is 'write', so we may not be able to read it.

with open(csv_filename_out, 'r') as f:
    print(f.read())
    print('donecheck')



    