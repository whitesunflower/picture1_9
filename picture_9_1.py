# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import sys, os


# 先将输入的图片填充为正方形
def fill_image(picture):
    width, height = picture.size
    new_image_length = width if width > height else height    # 选取长和宽中较大的值作为新图片的边长
    new_image = Image.new(picture.mode, (new_image_length, new_image_length), color='white')   # 创建一个白底图片
    if width > height:
        new_image.paste(picture, (0, int((new_image_length - height) / 2)))  # 填充height，居中
    else:
        new_image.paste(picture, (int((new_image_length - width) / 2), 0))    # 填充width，居中
    return new_image


# 分割图片（九宫格）
def cut_image(picture):
    width, height = picture.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j*item_width, i*item_width, (j+1)*item_width, (i+1)*item_width)  # (left, upper, right, lower)
            box_list.append(box)
    picture_list = [image.crop(box) for box in box_list]
    return picture_list


# 保存分割后的图片
def save_images(picture_list):
    index = 1
    for picture in picture_list:
        picture.save(str(index) + '.png', 'PNG')
        index += 1


# 分割后合成一张图（无缝隙）
def join_images(picture_list, picture):  # 此处的picture应该是已经填充为正方形的图片
    width, height = picture.size
    iw = int(width/3)  # 图片大小
    toImage = Image.new(picture.mode, (width, height), color='white')
    i=1
    for y in range(3):  # 一列放几张图
        for x in range(3):  # 一行放几张图
            fromImage = Image.open(str(i) + '.png')
            toImage.paste(fromImage, (x * iw, y * iw))  # 把fromImage粘到toImage上，（）里的为坐标
            i=i+1
    toImage.save('after.png')


# 分割后合成一张图（有缝隙）
def join_image(picture_list, picture):  # 此处的picture应该是已经填充为正方形的图片
    width, height = picture.size
    iw = int(width/3)  # 图片大小
    toImage = Image.new(picture.mode, (width+20, height+20), color='white')
    i=1
    for y in range(3):  # 一列放几张图
        for x in range(3):  # 一行放几张图
            fromImage = Image.open(str(i) + '.png')
            toImage.paste(fromImage, (x * iw+10 * x, y * iw+10 * y))  # 把fromImage粘到toImage上，（）里的为坐标
            i=i+1
    toImage.save('after.png')


if __name__ == '__main__':
    file_path = "R.jpg"
    image = Image.open(file_path)
    plt.imshow(image)
    plt.show()
    image = fill_image(image)
    # plt.axis('off')  # 除去坐标轴
    plt.imshow(image)
    plt.show()
    image_list = cut_image(image)
    save_images(image_list)
    # join_images(image_list, image)
    join_image(image_list, image)