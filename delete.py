# This program is to simply delete all the data from file
from sys import argv

script, filename = argv

xyz = open(filename,'w')
print("Here's your  file %r" % filename)
xyz.truncate()
