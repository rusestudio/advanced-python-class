import re

string = 'I like the mountain in the spring 98765'

print(re.findall('[a-zA-Z0-9]',string)) #[] make we can find in []  range

str2 = 'I have 12345 koalas!'
print(re.findall('[0-4]', str2))

str3 = 'You can see sea shells by the sea shore'
print(re.findall('.', str3))
print(re.findall('s.a', str3))
print(re.findall('s.{1}a', str3)) #start with s have 1 char in between, end with a
print(re.findall('s.{3}e', str3))

str4 = "Well will well... if it isn't Will Wilmwer"
print(re.findall('W.{2}l', str4)) #start with W have 2 char in btween, end with l

## $ =  the end on string
## ^ = beginning of string

s5 = 'Happy birthday to you. Happy birthday to you. Happy birthday dear Alex, happy  birthday to you.'
print(re.findall('^Happy', s5)) #only begin string
print(re.findall('^you', s5)) #cannot

print(re.findall('you.$', s5))
print(re.findall('$you.', s5)) # cannot

## * = zero or more
## + = 1 or more
## ? = zero or one

s6 = 'This Thing called a Thimble has Thrice hurt me'
print(re.findall('Thi.*', s6)) # from first Thi till more
print(re.findall('Thi.*s', s6)) # from Thi till very last s
print(re.findall('Thi.*e', s6)) 

s6 = 'This Thing called a Thimble ha Thrice hurt me'
print(re.findall('Thi.*s', s6)) #stil can print this coz * is zero or more

s6 = 'This Thing called a Thimble ha Thrice hurt me'
print(re.findall('Thi.+s', s6))# cannot print coz + is 1 or more
print(re.findall('Thi.+e', s6))

s6 = 'This Thing called a Thimble ha Thrice hurt me'
print(re.findall('Thi.?s', s6)) # print either have zero or 1 char
print(re.findall('Thi.{3}?e', s6))# print that have 3 char between


## | either or
s7 = 'I hate that I love ballon animals. They are beautiful.'
print(re.findall('hate|beautiful', s7))
print(re.findall('like|beautiful', s7))

## \ to get specific char
s8 = 'I like cats. You like cats. We all like cats.'
print(re.findall('\.', s8))


