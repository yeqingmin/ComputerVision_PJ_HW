import cv2

img = cv2.imread('C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg')

# 获取属性
# img.shape获取到当前行、列和通道的数量（如果是彩色的）
dimensions = img.shape
# print("图像的行列和通道数：" + dimensions)

# img.size获得到当前图像的大小：图像高度*图像宽度*图像通道数
element_total_num = img.size
# print("图像的大小" + element_total_num)

# img.dtype获取当前的图像数据类型
image_dtype = img.dtype
# print("图像数据类型" + image_dtype)

# 显示函数cv2.imshow()；该函数有两个参数，第一个参数是显示窗口的标题，第二个参数是要显示的图像
cv2.imshow('Original Image', img)

# 键盘绑定函数cv2.waitKey();为任何键盘事件等待指定的毫秒数。参数是以毫秒为单位的事件。当执行到此函数的时候，程序将暂停执行，当按下任何键后，程序将继续执行，如果毫秒数为0，它将无限期地等待键盘敲击事件：
# cv2.waitKey(1000)表示图片悬停一秒
cv2.waitKey(0)

# 获取图片中某个像素的b，g，r的值,x=40,y=6
(b, g, r) = img[6, 40]

# 仅获取蓝色
b = img[6, 40, 0]

# 仅获取绿色
g = img[6, 40, 1]

# 修改某点的颜色,像素值
img[6, 40] = (0, 0, 255)

# 获取某个区域的图象
top_left_corner = img[0:50, 0:50]

# 关闭所有窗口
cv2.destroyAllWindows()

# 灰度图像访问
gray_img = cv2.imread('C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg',
                      cv2.IMREAD_GRAYSCALE)

# 获取图像乔杜
i = gray_img[6, 40]
