class SchoolMember:
    '''代表任何学校里的成员。'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''代表一位老师。'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()


# 它是如何工作的
# 要想使用继承，在定义类时我们需要在类后面跟一个包含基类名称的元组。然后，我们会注
# 意到基类的 __init__ 方法是通过 self 变量被显式调用的，因此我们可以初始化对象的基
# 类部分。下面这一点很重要，需要牢记——因为我们在 Teacher 和 Student 子类中定义了
# __init__ 方法，Python 不会自动调用基类 SchoolMember 的构造函数，你必须自己显式地
# 调用它。
# 相反，如果我们没有在一个子类中定义一个 __init__ 方法，Python 将会自动调用基类的构
# 造函数。
# 我们会观察到，我们可以通过在方法名前面加上基类名作为前缀，再传入 self 和其余变
# 量，来调用基类的方法。
# 在这里你需要注意，当我们使用 SchoolMember 类的 tell 方法时，我们可以将 Teacher 或
# Student 的实例看作 SchoolMember 的实例。
# 同时，你会发现被调用的是子类型的 tell 方法，而不是 SchoolMember 的 tell 方法。理
# 解这一问题的一种思路是 Python 总会从当前的实际类型中开始寻找方法，在本例中即是如
# 此。如果它找不到对应的方法，它就会在该类所属的基本类中依顺序逐个寻找属于基本类的
# 方