
#variable
item = 'Banana'
Item = 'apple' #loweruppercase sensitive
item_name = 'orange' #space with _

print( item, Item, item_name)
print( 'Hello ' + item_name)

#data_type
integer =  2025
word = 'text'
isHappy = False #boolean
name_list = ['anna', 'mirae', 'dayana'] #array

print(integer)
print(word)
print(isHappy)
print(name_list)

integer = 20
name = 'mario'
string_num = '10'

print(name + str(integer)) #change int to string
print(10 + int(string_num)) #change string to int

a= 10
b= 5

add = a+b
dif = a-b
mul = a*b
div = a/b
power= a**b

print(add)
print(dif)
print(mul)
print(div)
print(power)

#logic_statement

age = 23
is_ok = True

if age > 20:        #if_else
    print('old')
elif age == 18:
    print('young')
else:
    print('baby')

if is_ok:
    print('ur  ok')
else:
    print('ur not ok')


#loop

for i in range(3):     #for i>0, i<3
    print('Hello', i)  # to start index from 1, i+1
    print('Hello', i+1)  # to start index from 1, i+1

print(range(3))
print(range(10))

#while loop

name_list2 =['ali', 'abu', 'anna']
for name in name_list2:
    print(name)

i =0
while i <5:  
    i = i+1
    print(i)

while True:
    user_input = input('enter text:') #get input
    if user_input =='0':
        print('exit')
        break


#function

def say_hello(person):
    print('hi', person)

say_hello('anna')
say_hello('police')

def start_game():
    pass           #to kiv method that we dont know yet

def score_game():
    pass

#try accept

number = input('enter number:')

try:
    print(int(number))
except:
    print('wrong type, not a number')

#random

import random
def ran():
    randnum = random.randint(1,45)
    return randnum


