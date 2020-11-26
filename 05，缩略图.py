from PIL import Image

#打开图片

image1 = Image.open('image/kq.jpg')       #给  image1 赋值

#设置尺寸
#thumbnail((宽高))
image1.thumbnail((150,150))


#显示
image1.show()


#保存
image1.save('image/suoxiao.jpg')