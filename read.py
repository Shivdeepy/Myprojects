# This program is to simply read the file contents. 
from sys import argv

script, filename = argv

xyz = open(filename)
print("Here's your  file %r" % filename)
print(xyz.read())

# Opening a file twice

abc = open(filename)
print("again opening ", filename)
print(abc.read())
