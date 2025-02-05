import numpy as np
import matplotlib.pyplot as plt

# 定义x的范围
x = np.linspace(0, 4 * np.pi, num=512)

y = np.sin(x)

# 绘制sin曲线，添加颜色、线型和标签
plt.plot(x, y, color='blue', linestyle='--', label='sin(x)')

# 添加标题和坐标轴标签
plt.title('Sine Wave')
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')

# 显示图例
plt.legend()

# 优化图形显示
plt.grid(True)
plt.tight_layout()

# 展示图形
plt.show()
