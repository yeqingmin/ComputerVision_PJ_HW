# 图像滤波
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgA = cv2.imread("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg")
imgA_RGB = imgA[:, :, ::-1]
# 实现一个5*5的高斯滤波器(sigma=2)

# 定义高斯核的尺寸
kernel_size = 4

# 定义高斯核中心点的坐标数组
x_indices = np.arange(-kernel_size//2, kernel_size//2 + 1)
y_indices = np.arange(-kernel_size//2, kernel_size//2 + 1)

# 创建二维坐标数组
x, y = np.meshgrid(x_indices, y_indices)

# 计算高斯核
sigma = 2
gaussian_kernel = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))

# 归一化高斯核
gaussian_kernel /= gaussian_kernel.sum()

# 打印高斯核
print(gaussian_kernel)

# 对图片A进行高斯滤波，得到B
imgB = cv2.filter2D(imgA_RGB, -1, gaussian_kernel)
imgB_RGB = imgB[:, :, ::-1]
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\question4_images\\gaussian.jpg", imgB_RGB)
# 显示图片A和图片B
plt.subplot(121), plt.imshow(imgA_RGB, cmap='gray'), plt.title('Image A')
plt.subplot(122), plt.imshow(imgB, cmap='gray'), plt.title('Image B')
plt.show()

# 定义拉普拉斯算子
laplacian_kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], dtype=int)

laplacian_kernel = np.float32(laplacian_kernel)

# 应用拉普拉斯滤波
imgC = cv2.filter2D(imgA_RGB, -1, laplacian_kernel)
imgC_RGB = imgC[:, :, ::-1]
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\question4_images\\laplacian.jpg", imgC_RGB)
# 显示图片A和图片C
plt.subplot(121), plt.imshow(imgA_RGB, cmap='gray'), plt.title('Image A')
plt.subplot(122), plt.imshow(imgC, cmap='gray'), plt.title('Image C')
plt.show()