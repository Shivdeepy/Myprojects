from sys import argv

script, filename = argv

x = open(filename,'w')
print("Here the file %r: " %filename)
x.truncate() # This command will erase all the data in the file

a = input("I am shiv")
b = input('Live in Gugaon')
c = input("27 years")

x.write(a)
x.write("\n")
x.write(b)
x.write(c)
x.write("\n")

#we can also directly write
x.write("I love my india")

x.close()

# Lets check what we write in file

y = open(filename)
print("Check file data")
print(y.read())