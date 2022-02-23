class Myclass:
    i = 12345

    def __init__(self):
        print('执行了构造函数')

    def func(self):
        return 'hello world'


x = Myclass()
print(x.i)
print(x.func())


class Krryclass:
    def __init__(self, one, two):  # self 代表的是类的实例
        self.o = one
        self.t = two
        print(self.__class__)


j = Krryclass(123, 456)  # 作为参数注入类的构造函数
print(j.o, j.t)


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0  # 两个下划线开头，声明该方法为私有属性或方法

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def __private_method(self):
        print('私有方法')

    def speak(self):
        self.__private_method()
        print('{name}说：我{age}岁，体重{weight}kg'.format(name=self.name, age=self.age, weight=self.__weight))


p = People('Krry', 25, 70)
p.speak()


# 类继承
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print('{name}说：我{age}岁，在读{grade}年级'.format(name=self.name, age=self.age, grade=self.grade))


p = Student('Krry', 25, 70, 5)
p.speak()


# 另一个类
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def lecture(self):
        print('我叫{0}，我是一个演说家，我演讲的主题是{1}'.format(self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample('Krry', 25, 70, 4, 'Python')
test.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法
test.lecture()

# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。当然也可以通过传递参数
numpo = 1


def changenum():
    global numpo
    print(numpo)
    numpo = 123


changenum()
print(numpo)


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

from datetime import date

now = date.today()
print(now)
print(date(2022, 2, 22))

print(list(range(1, 10)))
for x in range(1, 10):
    for y in range(1, x + 1):
        print('{}*{}={}\t'.format(y, x, x * y), end="")
    print()
