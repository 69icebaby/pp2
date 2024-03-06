#RegEx Python

import re

#Ex.1
t = input()
a = re.search("ab*", t)
print(a)

#Ex.2
t = input()
x = re.search(r"ab{2,3}", t)
print(x)

#Ex.3
t = input()
x = re.findall(r"[a-z_]+_[a-z]+",t)
print(x)

#Ex.4
t = input()
x = re.findall(r"[A-Z][a-z]+",t)
print(x)

#Ex.5
t = input()
x = re.findall(r".*a.*b$",t)
print(x)

#Ex.6
t = input()
x = re.sub(r"[., ]",":",t)
print(x)

#Ex.7
t = input()
x = re.sub(r"[_]","",t)
print(x)

#Ex.8
t = input()
x = re.findall(r"[^A-Z]*[A-Z][^A-Z]*",t)
result = ' '.join(x)
print(result)

#Ex.9
t = input()
x = re.findall(r"[A-Z][^A-Z]*",t)
res = ' '.join(x)
print(res)

#Ex.10
t = input()
x = re.sub(r"(?<!^)(?=[A-Z])","_",t).lower()
print(x)