from sys import argv
from os.path import exists

script, from_file, to_file = argv

x = open(from_file)
y = x.read()
print("The input is %d long"% len(y))

print("Does output file exists: %r" % exists(to_file))

a = open(to_file, "w")
a.write(y)

print("Done! ")

a.close()
x.close()

# Lets check the copied data 

z = open(to_file)
print(z.read())
