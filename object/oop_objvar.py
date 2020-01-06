class Robot:
    """表示有一个带有名字的机器人。"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()


# 它是如何工作的
# 这是一个比较长的案例，但是它有助于展现类与对象变量的本质。在本例中， population 属
# 于 Robot 类，因此它是一个类变量。 name 变量属于一个对象（通过使用 self 分配），因
# 此它是一个对象变量。
# 因此，我们通过 Robot.population 而非 self.population 引用 population 类变量。我们对
# 于 name 对象变量采用 self.name 标记法加以称呼，这是这个对象中所具有的方法。要记住
# 这个类变量与对象变量之间的简单区别。同时你还要注意当一个对象变量与一个类变量名称
# 相同时，类变量将会被隐藏。
# 除了 Robot.popluation ，我们还可以使用 self.__class__.population ，因为每个对象都通过
# self.__class__ 属性来引用它的类。
# how_many 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个
# classmethod（类方法） 或是一个 staticmethod（静态方法） ，这取决于我们是否知道我们需不需
# 要知道我们属于哪个类。由于我们已经引用了一个类变量，因此我们使用 classmethod（类方
# 法） 。
# 我们使用装饰器（Decorator）将 how_many 方法标记为类方法。
# 你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，因此启用
# @classmethod 装饰器等价于调用：
# how_many = classmethod(how_many)
# 面向对象编程
#
# 你会观察到 __init__ 方法会使用一个名字以初始化 Robot 实例。在这一方法中，我们将
# population 按 1 往上增长，因为我们多增加了一台机器人。你还会观察到 self.name 的值
# 是指定给每个对象的，这体现了对象变量的本质。
# 你需要记住你只能使用 self 来引用同一对象的变量与方法。这被称作属性引用（Attribute
# Reference）。
# 在本程序中，我们还会看见针对类和方法的 文档字符串（DocStrings） 的使用方式。我们可
# 以在运行时通过 Robot.__doc__ 访问类的 文档字符串，对于方法的文档字符串，则可以使用
# Robot.say_
