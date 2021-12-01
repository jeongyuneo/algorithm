import re

javaNaming = re.compile('([a-z]+([A-Z][a-z]*)*)')
cppNaming = re.compile('([a-z]+([_][a-z]+)*)')
snake_case = re.compile('_([a-z])')
camel_case = re.compile('[A-Z]')

def toJavaNaming(variable):
    return snake_case.sub(lambda x: x.group(0).replace('_', '') and x.group(1).upper(), variable)

def toCppNaming(variable):
    return camel_case.sub(lambda x: '_' + x.group().lower(), variable)

a = input()
if javaNaming.fullmatch(a):
    print(toCppNaming(a))
elif cppNaming.fullmatch(a):
    print(toJavaNaming(a))
else:
    print('Error!')