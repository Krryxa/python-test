# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
多行注释
哈哈哈哈
'''
print('name:', __name__)

if True:
    print('true')
    print('second')
else:
    print('false')

totalList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

print(totalList)

print('-----------字符串-----------')
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
test_str = '123456789'
print(test_str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(test_str[2:])  # 输出从第三个开始后的所有字符
print(test_str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(test_str * 2)  # 输出字符串两次
print('hello\nkrry')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nkrry')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input('\n\n按下 enter 键退出')  # 输出两个空行

# 同一行编写多条语句，用 ;
import sys;

x = 'krry';
sys.stdout.write(x + '\n')

print('不换行输出1', end="")
print('不换行输出2')

for i in sys.argv:
    print(i)
print('\nPython 路径为：', sys.path, '\n')

import import_test
import_test.print_func('舒其')
print(dir(import_test))

'''
在 python 用 import 或者 from...import 来导入相应的模块。
1. 将整个模块(somemodule)导入，格式为： import time
2. 从某个模块中导入某个函数,格式为： from time import sleep
3. 从某个模块中导入多个函数,格式为： from time import sleep, secondfunc, thirdfunc
4. 将某个模块中的全部函数导入，格式为： from time import *，在引用时格式为：sleep(1)
5. 将模块换个别名，例如：import time as abc，在引用时格式为：abc.sleep(1)
'''

# 当字符串内容为浮点型要转换为整型时，无法直接用 int() 转换：
# 需要把字符串先转化成 float 型再转换成 int 型：
print('字符串类型转换整型', int(float('2.3')))

print('-----------type-----------')
# python 中的变量不需要声明
count = 100  # 整型
miles = 903.12  # 浮点型
tgstr = '123joajieaef'  # 字符串
print(type(count))
print(type(miles))
print(type(tgstr))
print(isinstance(count, int))

print('-----------bool-----------')
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(issubclass(bool, int))
print(True == 1)  # True
print(False == 0)  # True
print(True + 1)
print(False + 1)
print(1 is True)  # False
print(0 is False)  # False

print('-----------加减乘除-----------')
print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4)  # 除法，得到一个整数，向下取接近商的整数
print(17 % 3)  # 取余
print(2 ** 10)  # 次方

aa, bb = 1, 'myWorld'  # 同时给多个变量赋值
print(aa, bb)
# 字符串不能被改变，向一个索引位置赋值，比如 bb[1] = 'm' 会导致错误


print('-----------list 列表-----------')
# list 列表
easeList = ['my', 123, 'krry', 456]
tinyList = ['continue', 789]
print(easeList)
print(easeList[0])
print(easeList[1:3])  # 从第二个开始输出到第三个元素
print(easeList[2:])  # 输出从第三个元素开始的所有元素
print(easeList * 2)  # 输出两次列表
print(easeList + tinyList)  # 链接列表

# 与字符串不一样，列表中的元素是可以改变的
easeList[0] = '改变0'
easeList.append('新增的')
easeList[1:3] = [1111, 'nonono']
print(easeList)
easeList[1:3] = []  # 将第二个开始到第三个元素设置为 []，也就是删去
print(easeList)
del easeList[1]  # 删除第二个元素
print(easeList)
print(len(easeList))  # 获取长度

numList = [0, 1, 2, 3, 4, 5]
# 在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取列表，得到 1, 3
print(numList[1:4:2])  # 输出[1, 3]

print('-----------tuple 元组-----------')
# tuple 元组
tupleinit = ('abcd', 786, 2.23, 'jjio', 70.2)
tinytuple = (123, 'continue')
print(tupleinit)  # 输出完整元组
print(tupleinit[0])  # 输出元组的第一个元素
print(tupleinit[1:3])  # 输出从第二个元素开始到第三个元素
print(tupleinit[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tupleinit + tinytuple)  # 连接元组
# 不能修改元组元素，也不能删除元组元素，可以整个删除元组
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tupleChange = ([1, 2, 3], 'ahhahah')
tupleChange[0][1] = 333  # 改变了元组里面 list 列表的第二个元素
print(tupleChange)
del tupleChange

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup0 = ()  # 空元组
tup1 = (20,)  # 只有一个元素的元组
print(tup0, tup1)

print('-----------set 集合-----------')
# Set 集合
# 可使用 {} 或 set() 函数创建集合。创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
mySet = {'google', 'taobao', 'jingdong', 'google'}
# or
mySet2 = set('abcdefg')
print(mySet)  # 输出集合，重复的元素被自动去重
print(mySet2)

if 'google' in mySet:
    print('google 在集合中')
else:
    print('google 不在集合中')

# 集合添加移除
mySet.add('添加的')
print(mySet)
mySet.update([1, 2, 3], [4, 5, 6])  # update 添加的元素可以是其他
print(mySet)
mySet.remove('添加的')
print(mySet)
mySet.clear()  # 清空元素，list列表、dict 字典也有。元组没有，因为元组不能修改和删除元素
print(mySet)

# set可以进行集合运算
aSet = set('abracadabra')
bSet = set('alacazam')
print(aSet)
print(aSet - bSet)  # aSet 和 bSet 的差集
print(aSet | bSet)  # aSet 和 bSet 的并集
print(aSet & bSet)  # aSet 和 bSet 的交集
print(aSet ^ bSet)  # aSet 和 bSet 中不同时存在的元素

print('-----------dict 字典-----------')
# Dictionary 字典
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
dict = {}  # 创建一个空字典
dict['a'] = 'a的值'
dict[2] = '2的值'

tinyDict = {'a': 'aaaa是python', 2: '22223333不会啊'}
print(dict['a'])  # 输出键为 a 的值
print(dict[2])  # 输出键为 2 的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值
del tinyDict['a']  # 删除键为 a 的元素
print(tinyDict)

print('-----------推导式-----------')
# 推导式
# 列表 list 推导式
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
thisnames = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_thisnames = [name.upper() for name in thisnames if len(name) > 3]
print(new_thisnames)

# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 集合推导式
# 计算数字 1,2,3 的平方数
numsep_nij = {i ** 2 for i in (1, 2, 3)}
print(numsep_nij)
# 判断不是 abc 的字母并输出：
noabcjih = {x for x in 'abracadabra' if x not in 'abc'}
print(noabcjih)

# 字典推导式
# 以 thisnames 元素为键，元素长度为值创建字段
thisnames_dict = {name: len(name) for name in thisnames}
print(thisnames_dict)
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
numsp_dict = {x: x ** 2 for x in (2, 3, 4)}
print(numsp_dict)
print(type(numsp_dict))

# 元组推导式
# 包含数字 1~9 的元组
oneanine = (x for x in range(1, 10))
print(oneanine)  # 返回的是生成器对象
# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(oneanine))

print('-----------逻辑运算-----------')
# 逻辑运算符，逻辑与：and，逻辑或：or，逻辑非：not
if (True and True):
    print('进来了')
if (True or False):
    print('进来了1')
if (not False):
    print('进来了2')
# 成员运算符：in：在指定序列；not in 不在指定序列
if ('a' in ('a', 'b')):
    print('在指定序列')
if ('b' not in ['a', 'c']):
    print('不在指定序列')

# 比较两个对象的存储单元
unitadrr, unitadrr2 = 20, 20
unitadrr3 = 30
if (unitadrr is unitadrr2):
    print('两个变量有相同标识')
if (unitadrr is not unitadrr3):
    print('两个变量没有相同标识')

# 删除引用
vae1 = 10
print(vae1)
del vae1
# print(vae1)   # NameError: name 'vae1' is not defined

print(str(unitadrr) + 'awefafwae')

print('-----------Fibonacci series: 斐波纳契数列-----------')
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=(','))
    a, b = b, a + b

print()
for i in ['a', 'b', 'c', 'd']:
    print(i, end=(','))
print()
for i in range(4):
    print(i, end=(','))
print()
for i in range(0, 10):
    print(i, end=(','))
print()
for i in range(0, 10, 3):  # 第三个参数是步长
    print(i, end=(','))
print()

print('-----------迭代器-----------')
# 是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
iterlist = [1, 2, 3, 4, 5]
itt = iter(iterlist)
print(next(itt))
print(next(itt))
for i in itt:
    print(i, end=(','))
print()

print('-----------函数-----------')


def maxx(a, b):
    if a > b:
        return a
    else:
        return b


fa, fb = 3, 6
print(maxx(fa, fb))


def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)

print('-----------列表当堆栈使用-----------')
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

print('-----------列表当队列使用-----------')
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)

print('-----------遍历技巧-----------')
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)
