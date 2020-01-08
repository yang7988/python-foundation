import json

d = dict(a=1, b=2)
str = json.dumps(d)
print(str)

e = json.loads(str)
print(e)
print(d == e)
print(type(e))
print(isinstance(e, dict))
