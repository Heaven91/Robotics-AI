# coding=utf-8
from pylab import *


def basic():
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    figure(figsize=(8, 6), dpi=80)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    subplot(1, 1, 1)

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plot(X, C, color="blue", linewidth=2, linestyle="-")

    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plot(X, S, color="green", linewidth=2, linestyle="-")

    # 设置横轴的上下限
    xlim(-4.0, 4.0)

    # 设置横轴记号
    xticks(np.linspace(-4, 4, 9, endpoint=False))

    # 设置纵轴的上下限
    ylim(-1.0, 1.0)

    # 设置纵轴记号
    yticks(np.linspace(-1, 1, 5, endpoint=True))

    # 以分辨率 72 来保存图片
    # savefig("exercice_2.png",dpi=72)

    # 设置图片边界，科学的方法
    xmin, xmax = X.min(), X.max()
    ymin, ymax = C.min(), C.max()

    dx = (xmax - xmin) * 0.1
    dy = (ymax - ymin) * 0.1

    xlim(xmin - dx, xmax + dx)
    ylim(ymin - dy, ymax + dy)

    # 在屏幕上显示
    show()


def axis_move():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5), dpi=80)
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label = "consine")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label = "sine")

    plt.xlim(X.min() * 1.1, X.max() * 1.1)
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min() * 1.1, C.max() * 1.1)
    plt.yticks([-1, 0, +1],
               [r'$-1$', r'$0$', r'$+1$'])

    # adding legend for this figure
    plt.legend(loc = 'upper left', frameon = False)

    plt.show()




# testing codes wrote above
basic()
axis_move()