# To access the elements of a list individually 
c1 = [1,'chandu',2,3,'mangu']
c2 = [[1,5,5,8],[6,66]]
c3 = ['!','@',5,'#']

for a in c1:
    print(a, end = "   ")

for b in c2:
    print("\n%r " %b)

	
# To create a list
elements = []

for i in range(0,6):
    print(" Adding %d to the list." %i)
    elements.append(i)

for i in elements:
    print('Element was:  %r  ' %i)
