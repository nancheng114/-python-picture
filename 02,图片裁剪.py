from PIL import Image

#打开图片

image1 = Image.open('image/kq.jpg')

#第二步，剪切图片
#crop((范围))   范围：左，上，右，下
#
image2 = image1.crop((115,20,500,400))
image2.show()
#保存图片
image2.save('image/jianqie.jpeg')

#

