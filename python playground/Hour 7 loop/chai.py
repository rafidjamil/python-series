# Behind the scene file

import time
print("chai is here")
username = "hitesh"
print(username)

# Open in integrated terminal

# Example - 01
# >>> f = open('chai.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("chai is here") \n'
# >>> f.readline()
# 'username = "hitesh"\n'
# >>> f.readline()
# 'print (username) '
# >>> f.readline()
# >>> f.readline()
# >>>

# Example - 02
# >>> f = open('chai.py')
# >>> f .__ next __ ()
# 'import time\n'
# >>> f .__ next __ ()
# 'print("chai is here") \n'
# >>> f .__ next __ ()
# 'username = "hitesh"\n'
# >>> f .__ next __ ()
# 'print (username) '
# >>> f .__ next __ ()
# Traceback (most recent call last) :
# File "<stdin>", line 1, in <module>
# StopIteration

# Example - 03
# for line in open('chai.py').readlines() its old method the readlines() takes more load in memory os instead of this we use below method

# >>> for line in open('chai.py'):
# print(line, end='')   //the end='' perform, it escapses all the gaped line in the output of after each line.

# import time
# print("chai is here")
# username = "hitesh"
# print (username)>>>

# Example - 04
# >>> f = open('chai.py')
# >>> while True:
# line = f.readline()
# if not line: break
# print(line, end='')

# import time
# print("chai is here")
# username = "hitesh"
# print (username)

# Example - 05
# >>> test = "hitesh"
# >>> if not test:
# print("chai")

# >>> test = ""
# >>> if not test:
# print("chai")
# ...
# ...
# chai

# Example - 06 for array.
# >>> myList = [1, 2,3, 4]
# >>> I = iter(myList)
# >>> I
# <list_iterator object at 0x102f4fa30>
# >>> I .__ next __ ()
# 1
# >>> :
# <list_iterator object at 0x102f4fa30>
# >>> I .__ next __ ()
# 2
# >>> I ._
# 3
# >>> I .__ next __ ()
# 4
# >>> I .__ next __ ()
# Traceback (most recent call last) :
# File "<stdin>", line 1, in <module>
# StopIteration
# H
# _next __ ()

# Example - 07
# >>> f = open('chai.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f .__ iter __ ()
# True

# Example - 08
# >>> myNewList = [1, 2,3]
# >>> iter(myNewList) is myNewList
# False

# Example - 09
# >>> D = {'a': 1, 'b':2}
# >>> for key in D.keys():
# print (key)
# a
# b
# >>> I = iter(D) //iter is a manual iterator
# >>> I
# <dict_keyiterator object at 0x102f81990>
# >>> next(I)
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# StopIteration

# Example - 10
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> I = iter(R)
# >>> next(I)

# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last) :
# File "<stdin>", line 1, in <module>
# StopIteration