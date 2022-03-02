# python_snippets

High level interpreted language

Primary Data types:
- Number
    - 3 types: Integers, floating point numbers, complex numbers
- Boolean
- String

Assigning new value to string does not change its value. Can be verified using id() method
```
str1 = "hello"
print(id(str1))

str1 = "bye"
print(id(str1))
print (str1)
```

Reverse indexing: Can do negative indexing
Slicing: Obtaining a portion (string) of a string by using its indices string[start:end]
Slicing with a step: string[start:end:step]
Reverse slicing: Can be used to return a reverse substring string[end:start:stepsize] (stepsize is negative)
Partial slicing: When one of the slicing parameters is not provided. string[:end], string[start:], string[:] (returns whole string), string[::-1] (returns whole string in reverse)

Floor division: Use the // operator. Eg. 56//10 = 5

"in" keyword used to check if one string exists in another. Applicable to tuples, lists, dictionary

"*" used to multiply strings and get a repeated pattern

"+" can be used to merge two strings, two lists, two tuples..

list: collection of values but values can be of any type. Also, lists are mutable.

join(): can be used to join multiple strings

format() :  can be used to format specified values and insert them in string's placeholders

```
"Good morning {0} and {1}".format("Mumbai", "Chicago")
```

lambda example:
```
cube = lambda num : num ^ 3
```

Function vs. Methods: One of the major differences is that for a method, the first argument is self.

list operations: remove(), append(), pop(), sort(), insert()

iteration: for a in alphabets

index(): gives us index of a particular value

Tuples: immutable. Very similar to list otherwise.

dict operations: del(). To use the deleted value use pop() or popitem()
iteration: dict.items() which returns (key,value) tuples

Set: Unordered collection of items
mutable data structures like lists or dictionaries can't be added to a set. Tuple can be.
Perfect data structure when you need simple existence check of items because it doesn't allow duplicates
discard() or remove() to remove items from set
add() or update()
difference () to get difference between two sets
| or union() to perform union
& or intesection() to perform intersection

