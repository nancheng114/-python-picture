from PIL import Image,ImageFont,ImageDraw

#打开图片
image1 = Image.open('image/kq.jpg')
# image1.show()


#创建字体

font = ImageFont.truetype('zt/青呱石头体.ttf',32)       #truetype(字体文件，字号)

#创建一个将文字写道图片上的对象

draw = ImageDraw.Draw(image1)            #Draw(目标图片)

#渲染文字
#有两种方法啊
#text(坐标，文字内容，文字颜色，字体类型)   这种方法顺序不能错
#text(坐标，文字内容，fill=文字颜色，font=字体类型)    这种方法  后面  两个位置能调换
draw.text((66,66),'刻晴',font=font,fill=(255,130,130,50))
draw.text((430,160),'七七',font=font,fill=(255,130,130,50))
draw.text((750,130),'莫娜',font=font,fill=(255,130,130,50))

#显示保存
image1.show()
image1.save('image/shuiying.jpg')