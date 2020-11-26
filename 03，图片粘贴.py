from PIL import Image

#准备图片
image1 = Image.open('image/kq.jpg')
image2 = Image.open('image/sy.jpg')


#粘贴 图片1.paste(图片2，(位置))
image1.paste(image2,(-100,10))      #将图片2粘贴到图片1中
image1.show()                       #展示图片