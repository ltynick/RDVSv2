"""
Optional: batch-resize images (e.g. for external stereo/depth tools).
NOT needed for basic frame extract + left crop (see USAGE.txt).
"""
import os

import cv2


def resizeFrameFolder(input_folder, output_folder, new_width, new_height):
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 构建输入和输出文件的路径
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            # 调用resize_image函数修改图片分辨率
            resize_image(input_image_path, output_image_path, new_width, new_height)


def resize_image(input, output, new_width, new_height):
    image = cv2.imread(input)
    new = cv2.resize(image, (new_width, new_height))
    cv2.imwrite(output, new, [cv2.IMWRITE_PNG_COMPRESSION, 0])


if __name__ == '__main__':
    # ----- USER: edit folders and target size -----
    input_folder = "./right/"
    output_folder = r"F:\RAFT-depth\right"
    new_width = 960
    new_height = 1080
    # ---------------------------------------------
    resizeFrameFolder(input_folder, output_folder, new_width, new_height)
    print("done!")
