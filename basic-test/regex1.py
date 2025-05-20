import re

quote = "there only. one thing i hate more. than one two lying one."

print(re.search("hate", quote))
print(re.search("hate", quote).group())

print(re.findall("one", quote))
print(len(re.findall("one", quote)))


print(re.split("one", quote))
print(re.split("\.", quote))

print(re.sub("one","many", quote))
print(re.sub("one","many", quote, count=1))