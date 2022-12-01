#----------->looping<---------------
'''for:-A for loop is used for iterating 
over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string)
'''

names = ["ram", "shyam", "ramu"]
for x in names:
  print(x)

'''Looping through a string.'''

for i in "apple":
    print(i)

'''The break statement'''

fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)
  if i == "banana":
    break

'''The continue statement.'''

ball = ["football", "hockey ball", "cricket ball"]
for i in ball:
  if i == "banana":
    continue
  print(i)

'''The range() function'''

for x in range(6):
  print(x)

'''Nested loop'''

colour = ["red", "blue", "pink"]
fruits = ["apple", "banana", "cherry"]

for x in colour:
  for y in fruits:
    print(x, y)


#--------->while loop<-----------

'''while:-
With the while loop we can execute a set of 
statements as long as a condition is true.
'''

i = 1
while i < 6:
  print(i)
  i += 1

'''The break statement'''

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

'''The continue statement'''

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)