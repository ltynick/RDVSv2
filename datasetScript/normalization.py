"""
Optional: normalize depth maps to 0–255 for visualization.
NOT needed for RGB-only workflow (see USAGE.txt).
"""
import os

import cv2
import numpy as np




def normDepthFolder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 构建输入和输出文件的路径
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            img = normDepth(input_image_path)
            # 修改分辨率
            # img = cv2.resize(img, (512, 384))
            cv2.imwrite(output_image_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def normDepth(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    max_v = img.max()
    min_v = img.min()
    img = (img - min_v) / (max_v - min_v)
    return img * 255


if __name__ == '__main__':
    # ----- USER: edit depth input/output folders (new_* unused here but kept for your edits) -----
    input_folder = r"F:\RAFT-depth\depth"
    output_folder = "./depth/"
    new_width = 512
    new_height = 384
    # -------------------------------------------------------------------------------------------
    normDepthFolder(input_folder, output_folder)
    print("done!")
