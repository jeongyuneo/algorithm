import re

lower_case = re.compile('[a-z]')
upper_case = re.compile('[A-Z]')
number = re.compile('[0-9]')
space = re.compile(' ')

while True:
    try:
        s = input()
        print(len(lower_case.findall(s)), len(upper_case.findall(s)), len(number.findall(s)), len(space.findall(s)))
    except:
        break