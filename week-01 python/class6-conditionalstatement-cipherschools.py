#----->Conditional Staement<------
#if,else and elif
'''If:-
It allows for conditional execution of a 
statement or group of statements based on the
 value of an expression.'''

a = 100
b = 200
if b > a:
  print("b is greater than a")

  '''elif:-
The elif keyword is pythons way
of saying "if the previous conditions 
were not true, then try this condition".
  '''

c = 100
d = 200
if d > c:
  print("b is greater than a")
elif c == d:
  print("a and b are equal")

'''else:-
The else keyword catches anything 
which isn't caught by the preceding
 conditions.
'''

e = 200
f = 33
if f > e:
  print("b is greater than a")
elif e == f:
  print("a and b are equal")
else:
  print("a is greater than b")