# -*- coding:UTF-8 -*-
import os
import shutil

# 文件夹路径变量定义
img_two_path = 'C:\\Users\\deeplove\\Desktop\\test\\img2'
img_three_path = 'C:\\Users\\deeplove\\Desktop\\test\\img3'

# 获得img2目录下的所有文件的文件名
# 文件名格式：img_19_2R9H.png
img_two_files = os.listdir(img_two_path)

count = 0

# 循环所有img2的文件名
for file_two_name in img_two_files:
    # 通过文件名截取序号，'img_' 与 '_26VH.png' 之间
    # 文件名格式：img_19_2R9H.png
    file_id = file_two_name[4:-9]  # 文件序号
    file_letter = file_two_name[-8:-4]  # 文件对应的验证码

    # 找到当前序号img3中的对应文件
    for i in range(0, 4):
        # 拆分后的文件名，img2文件夹中一个文件对应img3中4个文件
        file_img_three_name = 'img_' + file_id + '_' + str(i) + '.png'
        # 终点路径：路径 + 文件名
        # 应该放进去的文件夹路径，比如字母'A'图片放到 A文件夹
        img_destination_path = img_three_path + '\\' + file_letter[i:i + 1] + '\\' + file_img_three_name
        # 文件拷贝
        # 1、文件读取路径
        img_resource_path = img_three_path + '\\' + file_img_three_name
        # 2、拷贝文件操作
        shutil.copyfile(img_resource_path, img_destination_path)
        count = count + 1
        print('成功将复制图片%s到文件夹%s中' % (file_img_three_name, file_letter[i:i + 1]))

print('一共复制图片%d张' % count)
