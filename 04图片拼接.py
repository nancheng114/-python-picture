#图片拼接
from PIL import Image

#第一步，创建一个空白图
#模式有两种  RGB/RGBA   R=red  红色  G=green 绿色  B=blue  蓝色
#(红，绿，蓝) (255，0，0)红色 / (0,0,255)蓝色  /  (0,255,0)绿色
#(0,0,0)黑色   (255,255,255)白色

#创建一个空的容器
empty = Image.new('RGB',(1500,600),(255,255,255))           #empty 空的容器  new(模式，大小，颜色)


#第二步，打开两张图片
image1 = Image.open('../自我介绍/img/1.jpeg')
image2 = Image.open('../自我介绍/img/2.jpeg')
image3 = Image.open('../自我介绍/img/3.jpeg')
image4 = Image.open('../自我介绍/img/4.jpeg')

#第三步，把两张图片粘贴到空白图上
empty.paste(image1,(0,0))
empty.paste(image2,(700,0))
empty.paste(image3,(300,0))
empty.paste(image4,(300,200))


empty.show()        #empty为容器
