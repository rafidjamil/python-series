<!-- Hour 2 -->
# Object types / Data Types
- Number: 1234, 3.1654, 3+4j, 0b111, decimal(), fraction()

- String: "Hello", 'World', """Multiline String""", f"Formatted {value}"

- list : [1, 2, 3], ['a', 'b', 'c'], list(range(5))
# list Example 
<!-- mylist =[1,2,3,['a','b']]
>>> mylist
[1, 2, 3, ['a', 'b']] -->

- Tuple: (1, 2, 3), ('a', 'b', 'c'), tuple(range(5))
[brackets], (parabthesis), {curly braces}, <angle brackets>

- Dictionary: {'key1': 'value1', 'key2': 'value2'}, dict(a=1, b=2)
Dictionary have their index and value pair, key is unique and value can be duplicate.

- Set: {1, 2, 3}, {'a', 'b', 'c'}, set(range(5)) 

- file: file.txt, open('file.txt', 'r'), open('file.txt', 'w')

- Boolean: True, False, bool(1), bool(0)

- None: None, type(None)

- Function: modules, classes

- Advanced Data Types: Decorators, Generators, Iterators, Metaprogramming, Context Managers, Coroutines, Async/Await

<!-- Hour 3 -->
<!-- >>> import sys
>>> sys.getrefcount(2)
3221225472
>>> sys.getrefcount("Rafid")
3
>>> sys.getrefcount("Hi")
3
>>> sys.getrefcount(90)
3221225472 -->

#Eample 01
Python do not immediate garbage collector
a=2
a="rafid"
a=3.14
2 or "rafid" foran garbage may nhi jay ga balke python osy apne pas thori der kay lie save rakhe ga 

#Eample 02
>>> myListOne = [1,2,3]
>>> myListTwo = myListOne
>>> myListOne = "rafid"
>>> myListTwo
[1, 2, 3]

#Example 03
>>> myListOne = [1, 2, 3]
>>> myListTwo = myListOne
>>> myListOne = 'chai'
>>> myListTwo
[1, 2, 3]
>>> myListOne = [1, 2, 3] At this point, myListOne is a new list object, and myListTwo still refers to the original list object. Therefore, modifying myListOne will not affect myListTwo.
>>> myListTwo
[1, 2, 3]
>>> myListOne
[1, 2, 3]
>>> myListOne[0] = 33
>>> myListOne
[33, 2, 3]
>>> myListTwo
[1, 2, 3]

#Example 04
>>> 11 = [1, 2, 3]
>>> 12 = 11
>>> 11
[1, 2, 3]
>>> 12
[1, 2, 3]
>>> 11[0] = 44
>>> 11
[44, 2,3]
>>> 12
[44, 2,3]

#Slicing [0:2]
>>> l1=[1,2,3]
>>> l2=l1[0:2]
>>> l2
[1, 2]
>>> l1
[1, 2, 3]
>>> 

# Difference b/w == or is
== check the condition and is check the memory location of the object
>>> n = [1, 2, 3]
>>> m = n
>>> m
[1,2,3]
>>> n
[1, 2,3]
>>> m == n
True
>>> m is n
True
>>> n = [1, 2,3]
>>> m == n
True
>>> m = [1, 2,3]
>>> m == n
True
>>> m is n
False

Difference b/w repr(), str() and print()
>>> repr('chai') repr() object ki developer-oriented representation deta hai — aisi representation jo object ko clearly identify kare.
"'chai'"
>>> str('chai') str() object ko human-readable form mein convert karta hai.
'chai'
>>> print('chai') khalli walli print() function object ko console par print karta hai.
chai

I