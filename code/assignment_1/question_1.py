# 当前文件实现两张图片的拼接
from PIL import Image

# 打开两张图片
imgA = Image.open("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_1.jpg")
imgB = Image.open("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\images\\Image_2.jpg")

# 修改图片的尺寸为256*256，使用resize方法
# try:
imgA_resized = imgA.resize((256, 256))
# imgA_resized.save("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\images_revised"
#                  "\\Image1_revised.jpg")
# 保存新的图片
imgB_resized = imgB.resize((256, 256))
# imgB_resized.save("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\images_revised"
#                  "\\Image2_revised.jpg")
# except IOError:
#     print("Failed")

# 修改完之后进行图片拼接

# # Step1:创建一个新图像为512*256
# imgC = Image.new("RGB", (512, 256))
# # 将A放在C的左部分
# imgC.paste(imgA_resized, (0, 0))
#
# # 将B放在C的右部分
# imgC.paste(imgB_resized, (256, 0))
#
# # 保存ImgC
# imgC.save("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\images_revised"
#           "\\ImageC.jpg")

# imgC.show()

# 1.编写代码裁剪图片A。起始位置是(100, 50)，裁剪区域是：宽度200像素，高度150像素。
# 2.保存裁剪后的图片。
# 3.在笔记本中显示图片A和裁剪后的图片。

box = (100, 50, 200, 150)
imgD = imgA.crop(box)
imgD.save("C:\\Users\\lenovo\\Desktop\\Courses\\ComputerVision\\assignment1\\code\\images_revised"
          "\\ImageA_crop.jpg")
imgD.show()
