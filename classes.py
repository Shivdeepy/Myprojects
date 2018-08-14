class Employee:
    def __init__(self, first, last, pay):
	    self.first = first
	    self.last = last
	    self. pay = pay
	    self.email = first +'.'+ last + '@company.com'
		
    def fullname(self):
	    return '{} {}'.format(self.first, self.last)
		
    def tax(self):
	    return self.pay * 0.15
		
		
	
emp_1 = Employee('shivdeep', 'Kuma', 30000)
emp_2 = Employee('Gopal', 'Singh', 50000)

# Case 1
print (emp_1.fullname())

# Case 2
print (Employee.fullname(emp_1))

# Case 3
halu = Employee
print (halu.fullname(emp_1))

# Case 1 , Case 2 and Case 3 have same output. 


print (emp_2.tax())



print (emp_1.pay)
print (emp_2.last)
