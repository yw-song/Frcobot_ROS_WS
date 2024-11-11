import numpy as np

# 已知的三个点
x_points = np.array([0, -26.5, 26.5])
y_points = np.array([0, -1, -1])
z_points = np.array([0, -1, -1])

# 方程的系数矩阵 [a, b, c]
A = np.array([
    [x_points[0]**2, x_points[0], 1],  # 对应点 (0, 0)
    [x_points[1]**2, x_points[1], 1],  # 对应点 (-26.5, -1)
    [x_points[2]**2, x_points[2], 1],  # 对应点 (26.5, -1)
])

# 右侧向量
B = np.array([z_points[0], z_points[1], z_points[2]])

# 解线性方程求a、b和c
coeffs = np.linalg.solve(A, B)

# 得到的系数
a = coeffs[0]
b = coeffs[1]
c = coeffs[2]

# 输出拟合出的抛物线方程
print(f"拟合出的抛物线方程为: z = ({a:.4f}) * x^2 + ({b:.4f}) * x + ({c:.4f})")

# 旋转成抛物面方程
# r = sqrt(x^2 + y^2)，抛物面方程为 z = a * r^2 + b * r + c
# 其中r是极坐标中的半径

# 输出空间抛物面方程
print(f"抛物面方程为: z = ({a:.4f}) * r^2 + ({b:.4f}) * r + ({c:.4f})")
