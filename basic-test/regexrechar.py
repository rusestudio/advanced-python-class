import re

s1 = 'My name is Neo. My phone number is 010-3241-8890. My email is TheNeo@gmail.com'

# \d to get digit
print(re.findall('\d',s1))
print(re.findall('\d{3}',s1))
print(re.findall('[0-9]{3}',s1))

# \D get non-digit
print(re.findall('\D',s1))

# \w only char no sign
print(re.findall('\w',s1))

# \W only sign no char
print(re.findall('\W',s1))

# \s get white space, tab, newline
print(re.findall('\s',s1))

# \S get everything  but the white space
print(re.findall('\S',s1))

# \A = ^
# \Z = &
print(re.findall('\A[A-Za-z]',s1))
print(re.findall('[A-Za-z]\Z',s1))

# b search for boundary when it is preceded by a non-word character.(space)
# B non boundary
s2 = 'I love the Matrix is the MatrixLove a word?'
print(re.findall(r'\bMatrix\b',s2))
print(re.findall(r'\bMatrix',s2))
print(re.findall(r'\Batrix',s2))