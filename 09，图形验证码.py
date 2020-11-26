from PIL import Image,ImageDraw,ImageFont,ImageFilter
#ImageDraw,ImageFont  写文字   ImageFilter   添加滤镜

import random

#创建空画布
image1 = Image.new('RGBA',(120,60),(125,145,246))

#创建一个画画的对象
draw = ImageDraw.Draw(image1)


#渲染背景
def a():
    return random.randint(1,255),random.randint(1,255),random.randint(1,255)

#导入random库之后，在1.255之间随机选择一个数，选3次

# print(a())
for x in range(0,120):        #线汇成面
    for y in range(0,60):    #点汇成线
        draw.point((x,y),a())


#加一个渲染效果
# image1 = image1.filter(ImageFilter.BLUR)


#渲染文字
#创建文字对象
font = ImageFont.truetype('zt/青呱石头体.ttf',30)

#将0-9直接任意数字  4次写入上面的背景中
for i in range(4):
    y= random.randint(10,10)
    x = str(random.randint(0,9))        #str()由数值转换成字符串
    draw.text((i*30, y),x,font=font,fill=a())
#显示保存
image1.show()