import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 解决中文乱码，设置默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 2, 100)  # 创建等差数列 0-2之间100个

# 绘制子图，参数位置
# plt.subplot(1, 2, 1)

plt.plot(x, x, label="line1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
plt.plot(x, x ** 2, label="line2")
plt.plot(x, x ** 3, label="line3")
plt.xlabel("x label")  # x轴名字
plt.ylabel("y label")  #  y轴名字
plt.title("折线图")  #  图标名字
plt.legend()  #  显示图例


# 柱状图
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# 生成另一张图
plt.subplots()
# 绘制子图，参数位置
# plt.subplot(1, 2, 2)

# 创建条形图
plt.bar(y_pos, height, label='bar1')
# x轴标签
plt.xticks(y_pos, bars)
plt.title("柱状图")
plt.legend()

plt.show()  #  生成图表
