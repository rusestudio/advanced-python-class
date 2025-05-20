#int class
print(int(1.23))
print(int("123"))
print(int(True))
print(int(123))

#float class
print(float('123'))
print(float(10))
print(float(True))
print(float(1.23))

#string class
print(str(100))
print(str(1.0))
print(str(True))
print(str("hello"))

#boolean class
print(bool(1))
print(bool(123.123))
print(bool("False"))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool('0'))
print(bool(""))

#hex class
#get int to hex
print(hex(0))
print(hex(1))
print(hex(10))
print(hex(123))

#oct class
#get int to oct
print(oct(0))
print(oct(1))
print(oct(10))
print(oct(123))

#bin class
#get int to binary
print(bin(0))
print(bin(1))
print(bin(10))
print(bin(123))

#list class
#get empty list and return  
print(list())
print(list((1,2,3)))
print(list((1,2,3,2,1)))

#set class
print(set())
print(set((1,2,3)))
print(set((1,2,3,2,1)))

#tuple class
print(tuple())
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#dic class
#return dictionary
print(dict())
print(dict(one=1, two=2, three=3))
print(dict([('two', 2), ('one', 1), ('three', 3)])) #passing a list of tuples to the dict() constructor.

#range class
#The range([start,] stop [,step]) function:
#Generates a sequence of consecutive numbers
##Starts from [start] (if provided, otherwise defaults to 0)
#Ends at stop - 1 (the stop value is excluded)
#Increments by step (if provided, otherwise defaults to 1)
#Returns an iterable containing the generated sequence.
print(range(10))
print(list(range(4,7)))
print(list(range(5,10)))
print(list(range(0,-10,-1)))

#map class
#`map(f, iterable)` takes a function and an iterable object as input,
# then applies the function `f` to each element of the iterable
# and returns the results as a collection.
def two_times(x):
    return x*2
r=list(map(two_times, [1,2,3,4]))
print(r)

#len()
#get length 
print(len("abc"))
print(len([1,2,3]))
print(len({1,2,3}))

#all()
#- `all(iterable)` takes an **iterable** as input and 
# returns **`True`** if **all** elements in the iterable are `True`.  
# If the **iterable is empty**, it returns **`True`**.
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([]))

#any()
#even 1 input is true, result true
#if list empty = false
print(any([1,2,3,0]))
print(any([0, ""]))
print(any([]))

#abs class
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#pow class
print(pow(2,4))
print(pow(3,3))
print(pow(5,2))

#round class
print(round(1.6))
print(round(1.2))
print(round(1.234,2)) #round(x, n): Rounds x to n decimal places
print(round(1.678,1))

#max class
#max([1,2,3])	List	Largest number	3
#max("python")	String	Highest ASCII character	'y'
#max({1:3, 2:'a'})	Dictionary	Largest key	2
print(max([1,2,3]))
print(max("python"))
print(max({1:3, 2:'a'})) #1 & 2 is key

#min class
print(min([1,2,3]))
print(min("python"))
print(min({1:3, 2:'a'}))

#sum class
print(sum([1,2,3]))
print(sum((4,5,6)))
print(sum({1:3, 2:'a'}))
print(sum({1,2}))

#reversed class
print(reversed(["a", "b", "c", "d"]))
print(list(reversed(["a", "b", "c", "d"])))


#sort class
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

#filter class
#only return true element
def positive(x):
  return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

#lambda

#usual way
def hap(x, y):
  return x + y
print(hap(10, 20))

#lambda way
print((lambda x,y: x + y)(10, 20))

print(lambda x: x + 10)

# 람다식으로 만든 함수를 호출하려면 람다 표현식을 변수에 할당해야 함
plus_ten = lambda x: x + 10
print(plus_ten(1))

f = lambda x, y: x+y
print(f( 10, 20 ))

#람다식을 ( )(괄호)로 묶은 뒤에 다시 ( )를 붙이고 인수를 넣어서 호출하면 됨
print((lambda x: x + 10)(1))

#cannot declare var in lambda instead below
y = 10
print((lambda x: x + y)(1))