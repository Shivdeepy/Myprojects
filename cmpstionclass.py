class Other(object):

    def override(self):
	    print("OTHER override()")
		
    def implicit(self):
	    print("OTHER implicit()")
		
    def altered(self):
	    print("OTHER altered()")
		
class Child(object):

    def __init__(self):
	    self.other = Other()
		
	#def __init__(self):
	#    pass
		
    #other = Other()
			
    def implicit(self):
	    self.other.implicit()
		
    def override(self):
	    print("CHILD override()")
		
    def altered(self):
	    print("CHILD, Before Other altered()")
	    self.other.altered()
	    print("CHILD, After Other altered()")
		
son = Child()

son.implicit()
son.override()
son.altered()
