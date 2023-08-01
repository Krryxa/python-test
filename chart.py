import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 解决中文乱码，设置默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 2, 100)  # 创建等差数列 0-2之间100个

plt.plot(x, x, label="line1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
plt.plot(x, x ** 2, label="line2")
plt.plot(x, x ** 3, label="line3")
plt.xlabel("x label")  # x轴名字
plt.ylabel("y label")  #  y轴名字
plt.title("折线图")  #  图标名字
plt.legend()  #  显示图例
plt.show()  #  生成图表
