from PIL import Image,ImageDraw
import random
#因为random是一个新的库，所以要换行重新导入

#创建画布

image1 = Image.new('RGB',(800,800),(250,250,250))
# image1.show()

#创建一个画画的人

draw = ImageDraw.Draw(image1)


#画颜色    point((坐标),(颜色))
# draw.point((10,10),(50,80,90))
# draw.point((50,10),(89,12,12))
# draw.point((80,80),(22,23,88))
# draw.point((60,20),(97,55,21))
# draw.point((90,30),(12,40,132))
# draw.point((20,80),(78,78,170))
# draw.point((40,50),(65,98,78))
# draw.point((40,60),(45,45,12))
# draw.point((80,90),(36,255,147))

#画条线
# for x in range(100,601):
#     draw.point((100,x),(255,0,0))
#     draw.point((101,x),(255,0,0))
#     draw.point((102,x),(255,0,0))


#画条线，变成面
# for i in range(100,601):
#     for a in range(100,601):
#         draw.point((i,a),(255,0,0))



# print(random.randint(1,33))     #1到33随机取一个数

def a():
    return random.randint(1,255),random.randint(1,255),random.randint(1,255)
#导入random库之后，在1.255之间随机选择一个数，选3次

# print(a())
for x in range(100,601):        #线汇成面
    for y in range(100,501):    #点汇成线
        draw.point((x,y),a())


#   展示
image1.show()