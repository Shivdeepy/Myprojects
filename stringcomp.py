s = 'CCCCAAAATTTT'
x = 'CAT'

i = 0
a = 0

while i < len(s):
    if s[i] != 'C':
        a = a + 1
    if s[i+1] != 'A':
        a = a +1
    if s[i+2] != 'T':
        a = a + 1

    i=i+3
  
print(a)
