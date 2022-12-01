#Taking input from user
a=input()
b=input("Enter your name:")
print(type(a))
#default datatype of input value is <string> str

#to take integer input
c=int(input("Enter your number:"))
print(type(c))
#type will be int

#to take float input
d=float(input("Enter your number:"))
print(type(d))
#type will be float

#-------->Typecasting<--------
'''The conversion of one data type into the other 
data type is known as type casting in python or type conversion'''

z=input("Enter a number")
x=int(z) #string converted to integer
y=float(x) #integer converted to float
w=complex(y) #float value converted to complex number
r=str(w) #complex number converted to string