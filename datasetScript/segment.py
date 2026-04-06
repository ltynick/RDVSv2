import os

from PIL import Image

# ----- USER: edit paths (see USAGE.txt) -----
PATH_IMG = "./left-right"  # side–by–side frames from cutImage.py (or your own full-width stereo pairs)
PATH_LEFT = "./left"  # output: left half (typical “left view” RGB)
PATH_RIGHT = "./right"  # output: right half; optional / can delete files if unused
# -------------------------------------------

os.makedirs(PATH_LEFT, exist_ok=True)
os.makedirs(PATH_RIGHT, exist_ok=True)
img_dir = [f for f in os.listdir(PATH_IMG) if os.path.isfile(os.path.join(PATH_IMG, f))]
print(img_dir)
print(len(img_dir))
for i in range(len(img_dir)):
    # 获取初始图片名作为id
    id = img_dir[i].split(".")[0]
    img = Image.open(os.path.join(PATH_IMG, img_dir[i]))
    size_img = img.size
    print(size_img)
    # 左右各一半：宽 // 2
    weight = int(size_img[0] // 2)
    height = int(size_img[1])

    box = (weight * 0, height * 0, weight * 1, height * 1)
    region = img.crop(box)
    region.save(os.path.join(PATH_LEFT, "{}.png".format(id)))
    box2 = (weight * 1, height * 0, weight * 2, height * 1)
    region2 = img.crop(box2)
    region2.save(os.path.join(PATH_RIGHT, "{}.png".format(id)))

