import cv2
from matplotlib import pyplot as plt
# 首先读取当前图像
img = cv2.imread('C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg')

# 然后将该图片按照BGR的顺序分割图像，分成三个通道
b, g, r = cv2.split(img)

# 合并通道，按r,g.b合并，得到需要的Matplotlib格式
img_matplotlib = cv2.merge([r, g, b])


# 使用Matplotlib绘制图像

# subplot将多个图像放在一个窗口中，subplot中可以使用三个参数，subplot(m, n, p)，子图处理m*n网格中的图，m确定行数、n确定列数，p确定要在网格中放置图的位置
# 121表示一行有两列，当前元素为第一行第一个元素
# plt.subplot(121)
# plt.imshow(img)
# # 122表示一行有两列，当前元素为第一行第二个元素
# plt.subplot(122)
# plt.imshow(img_matplotlib)
# plt.show()

# 使用cv展示图像
cv2.imshow('BGR in OpenCV', img)
cv2.imshow('RGB in OpenCV', img_matplotlib)
cv2.waitKey(0)

# 如果想要快速将OpenCV中的BGR转换成RGB让matplotlib来显示，可以使用以下的代码
# img_matplotlib = img_opencv[:, :, ::-1]
