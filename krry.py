abc = '输出的值\n'

thisabc = repr(abc)
print(thisabc)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x ** 2).rjust(3), end=" ")
    print(repr(x ** 3).rjust(4))

# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
# 在括号中的数字用于指向传入对象在 format() 中的位置
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x ** 3))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址：{site}'.format(name='krryblog', site='ainyi.com'))
# 位置及关键字参数可以任意的结合
print('{0} {1} {name}'.format('ooo', 'ppp', name='hahha'))

import math

print('常量 PI 的值近似为： {}'.format(math.pi))
# 保留小数点后三位
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ===> {1:10d}'.format(name, number))

print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# 左边填充 0
print('123'.zfill(5))

# inputstr = input('请输入内容：')
# print('你输入的内容是：', inputstr)

print('---------文件---------')

fw = open('test.md', 'w')  # r 只读，w 只写，a 追加，r+ 同时用于读写。 r 是默认值
fw.write('krry 帅爆了.\n真的是帅疯了！！')
fw.close()

fa = open('test.md', 'a')
fa.write('krry 帅爆了追加')
value = ('ainyi.com', 124)
fa.write(str(value))
fa.close()

fr = open('test.md')
print(fr.read())
fr.close()
fr = open('test.md')
print(fr.readline())
fr.close()
fr = open('test.md')
print(fr.readlines())
fr.close()
fr = open('test.md')
fr.seek(5)
print('移动5个字符，读取第一行：', fr.readline())
fr.close()

# 迭代一个文件对象读取每行
fr = open('test.md')
for line in fr:
    print(line, end='')  # end='' 意思是不换行，末尾加'' 

print()

print('---------异常 try except---------')
# try：执行代码 except：捕获异常 finally：不管有没有异常都执行
while True:
    try:
        x = int(input('请输入一个整数'))
        break
    except ValueError:
        print('你输入的不是整数')
        raise Exception('我需要一个整数！！！')  # 抛出异常

try_file = open('./test.txt', 'w')
try:
    try_file.write('hello world')
finally:
    try_file.close()  # 要手动调用 f.close() 方法关闭

print('---------异常 with---------')
# 使用 with 关键字系统会自动调用 f.close() 方法
with open('./test.txt', 'w') as with_file:
    with_file.write('hello world !')
print('文件是否关闭：', with_file.closed)
