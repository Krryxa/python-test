def print_func(c):
    print('hello:', c)
    if __name__ == '__main__':
        print('程序自身在运行')
    else:
        print('来自外部模块运行')
    return


print_func('self')