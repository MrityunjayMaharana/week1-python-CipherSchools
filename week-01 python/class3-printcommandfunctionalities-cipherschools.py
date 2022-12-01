print("My name")
#Normal print statement

print(1,2,3,"cat")
#output--->1 2 3 cat

print(1,2,3,"cat",sep=",")
#output--->1,2,3,cat

print("hello")
print("world!")
'''output--->hello
             world!
'''
print("hello",end=";")
print("world!")
#output--->hello;world!


print("a")
print("b")
print("c")
'''output--->a
             b
             c
'''
print("a",end=")")
print("b",end=")")
print("c")
#output--->a)b)c