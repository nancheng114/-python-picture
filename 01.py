#安装  pip install pillow

from PIL import Image,ImageFilter
#按住ctrl，点击ImageFilter可进入

#====打开的图片.fillter(滤镜效果)     返回给你一个新的图片

#1  加载图片  打开图片
#image1 = Image.open('image/kq.jpg')


#相对路径和绝对路径
image1 = Image.open('image/psc (13).jpeg')         #相对路径
# image1 = Image.open('C:/Users/南城/Desktop/自我介绍/img/xx.jpg')     #绝对路径
#同一盘符可以用相对路径，不同盘符必须用绝对路径

#../ 上一级
#../../上二级
#./当前文件夹下面

# #2,显示图片
image1.show()
#
# #3, 保存图片
# image1.save('image/dgz.jpg')


#浮雕效果
# image2 = image1.filter(ImageFilter.EMBOSS)#吧步骤1打开的图片进行处理放到image2中
# image2.show()
#
# # #  保存图片
# image2.save('image/fudiao.jpg')



# 铅笔画
# image3 = image1.filter(ImageFilter.CONTOUR)   #把步骤1打开的图片放到image3中
# image3.show()
# image3.save('image/qianbi.jpg')

# #  保存图片



#模糊
# image4 = image1.filter(ImageFilter.BLUR)        #把步骤1打开的图片放到image4中
# image4.show()                                   #显示image4
# image4.save('image/mohu.jpg')


#锐化
# image5 = image1.filter(ImageFilter.EDGE_ENHANCE)        #把步骤打开的图片放到image5中
# image5.show()                                            #显示image5
# image5.save('image/ruihua.jpg')

#
# image6 = image1.filter(ImageFilter.SHARPEN)        #把步骤打开的图片放到image6中
# image6.show()                                            #显示image6
# image6.save('image/cs.jpg')

#自定义效果
# class WH_PYTHON(ImageFilter.BuiltinFilter):
#     name="WH_Python"
#     filterargs = (3,3),1, 0,(
#         1,1,1,
#         1,-7,1,
#         1,1,1,
#     )
#
# image7 = image1.filter(WH_PYTHON)
# image7.show()