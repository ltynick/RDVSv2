import os

from PIL import Image

# ----- USER: edit paths and crop (see USAGE.txt) -----
PATH_IMG = "./cutImage/"  # input: full frames (e.g. copy from image/<VIDEO_ID>/ here)
PATH_OUT = "./left-right/"  # output: cropped frames before left/right split
# Crop: strips top/bottom; tune divisor if black bars differ for your videos
REDUCTION_H_DIVISOR = 7.8
# ----------------------------------------------------

os.makedirs(PATH_OUT, exist_ok=True)
img_dir = [f for f in os.listdir(PATH_IMG) if os.path.isfile(os.path.join(PATH_IMG, f))]
print(img_dir)
print(len(img_dir))
for i in range(len(img_dir)):
    # 获取初始图片名作为id
    id = img_dir[i].split(".")[0]
    img = Image.open(os.path.join(PATH_IMG, img_dir[i]))
    size_img = img.size
    print(size_img)
    # 准备将图片切割成4张小图片,这里后面的2是开根号以后的数，比如你想分割为9张，将2改为3即可
    # reduction_w = int(size_img[0] // 73)
    reduction_h = int(size_img[1] // REDUCTION_H_DIVISOR)
    weight = int(size_img[0])
    height = int(size_img[1])

    # box = (weight * 0 + reduction_w, height * 0 + reduction_h, weight * 1 - reduction_w, height * 1 - reduction_h)
    box = (weight * 0, height * 0 + reduction_h, weight * 1, height * 1 - reduction_h)
    region = img.crop(box)
    region.save(os.path.join(PATH_OUT, "{}.png".format(id)))
