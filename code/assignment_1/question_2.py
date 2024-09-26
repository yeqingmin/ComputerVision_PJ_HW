# 任务二：将A图片转换成灰度图像B
# 将灰度图像B转换成二值图像C
# 将A从RGB空间转换成HSV空间，显示A和A的转换结果（subplot）
import cv2
import matplotlib.pyplot as plt

imgA = cv2.imread("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg")

imgB = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\question2_images_revised"
            "\\ImageB_GRAY.jpg", imgB)

# 将灰度图像B转换成二值图像C,阈值为127
_, imgC = cv2.threshold(imgB, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\question2_images_revised"
            "\\ImageC_BINARY.jpg", imgC)

# cv2.imshow("Original Image", imgA)
# cv2.imshow("Revised Image", imgB)
# cv2.imshow("Binary Image",imgC)
# cv2.waitKey(0)

# 将图片A转换成HSV的图像并通过subplot一同显示
imgA_RGB = imgA[:, :, ::-1]

imgA_HSV = cv2.cvtColor(imgA, cv2.COLOR_BGR2HSV)

plt.subplot(1, 2, 1), plt.imshow(imgA_RGB)
plt.subplot(1, 2, 2), plt.imshow(imgA_HSV)

plt.show()
