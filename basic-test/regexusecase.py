import re

txt = '''
My name is Mr. Neo. My phone number is 123-456-7890. My email is ChosenOne@gmail.com
My name is Mr. Morphius. My phone number is 413-234-5677. My email is CoolGuy@yahoo.com
My name is Mrs. Trinity. My phone number is 765-456-8902. My email is ChosenOnesGirl1@apple.com
'''

print(re.findall('@[a-z]+', txt))
print(re.findall('@([a-z]+)', txt)) # find only in () group
print(re.findall('@([\w\.]+)', txt))
print(re.findall('[\w+]+@[\w\.]+', txt))

print(re.findall('\d{3}-\d{3}-\d{4}', txt)) #find phone num

txt_list = ['ChosenOne@gmail.com', 'CoolGuy@yahoo.com', 'ChosenOnesGirl1@apple.com']

#loop through re in list
for email in txt_list:
    print(re.findall('@([\w\.]+)',email))

domain_list = [re.findall('@([\w\.]+)',email)[0] for email in txt_list] # can use in dict too
print(domain_list)
