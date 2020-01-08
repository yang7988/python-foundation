import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Bob", 20, 88)


# print(json.dump(s)) 会报错，需要把对象转换成dict字典对象

def student2dict(std):
    return {
        "name": std.name,
        "age": std.age,
        "score": std.score
    }


str = json.dumps(s, default=student2dict)
s = json.dumps(s, default=lambda obj: obj.__dict__)
print(str)
print(s)


def dict2student(d):
    return Student(d["name"], d["age"], d["score"])


d = json.loads(s, object_hook=dict2student)
print(d)
