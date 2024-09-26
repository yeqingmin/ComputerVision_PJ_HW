# 图像直方图
import cv2
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

imgA = cv2.imread("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg")

# 将A转成灰度图像B
imgB = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)

# 提取B的直方图：绘制灰度图像的直方图只需要单通道，不需要rgb三个通道
# 单通道的直方图
hist = cv2.calcHist([imgB], [0], None, [256], [0, 256])  # 计算直方图
plt.hist(imgB.ravel(), 256)  # 绘制直方图。# img.ravel() 将图片转化成一维数组; 256 是BIN的数目
plt.show()

# 使用pillow将这些信息绘制为图片C

# 创建一个新的白色图像
# 归一化直方图
hist_norm = cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

# 创建一个空白的图像
imgC = np.zeros_like(imgB)

# 重建图像
for i in range(256):
    count = np.sum(hist_norm[i].astype(np.uint8))
    thresh = imgB >= i
    imgC[thresh] = i

# 将numpy数组转换为Pillow图像
imgC = Image.fromarray(imgC)

# 保存或显示图像
imgC.save('C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\question3_images\\ImageC_histogram'
          '.png')
imgC.show()

