from PIL import Image

#加载图片
image1 = Image.open('image/kq.jpg')
image2 = Image.open('image/kq1.jpg')


# #左右镜像
# image_lr=image1.transpose(Image.FLIP_LEFT_RIGHT)    #左右翻转
# image_lr.show()
# #保存
# image_lr.save('image/jingxiang.jpg')
#
# #上下镜像
# image_lr=image2.transpose(Image.FLIP_TOP_BOTTOM)    #上下翻转
# image_lr.show()
# #保存
# image_lr.save('image/shangxia.jpg')

#直接倒过来，先左右在上下
#左右镜像
image9=image1.transpose(Image.FLIP_LEFT_RIGHT)
#左右翻转     用image9当作一个空值，将翻转过后的image1  传递给image9，然后输出image9
#            输出后image1为空值

#上下镜像
image1=image9.transpose(Image.FLIP_TOP_BOTTOM)
#上下翻转     将上面赋值的image9进行翻转，反转完成后传递给imange1
#           （imange1在上面已经为空值，可以替换成其他名字）

#保存
image1.save('image/diandao.jpg')

#显示
image1.show()

