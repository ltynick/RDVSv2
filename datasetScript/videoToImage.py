"""
Video <-> frames helpers. Main entry: run as script (see USAGE.txt).
"""
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image


def Pic2Video():
    # USER: legacy helper; set paths before use
    imgPath = "youimgPath"  # 读取图片路径
    videoPath = "youvideoPath"  # 保存视频名称，路径默认为当前文件夹下

    images = os.listdir(imgPath)
    # 如果视频出现乱帧的情况，采用如下函数可以改正
    images.sort()

    fps = 25  # 每秒25帧数

    # VideoWriter_fourcc为视频编解码器 ('I', '4', '2', '0') —>(.avi) 、('P', 'I', 'M', 'I')—>(.avi)、('X', 'V', 'I', 'D')—>(.avi)、('T', 'H', 'E', 'O')—>.ogv、('F', 'L', 'V', '1')—>.flv、('m', 'p', '4', 'v')—>.mp4
    fourcc = VideoWriter_fourcc(*"MJPG")

    h, w, _ = cv2.imread(os.path.join(imgPath, images[0])).shape

    videoWriter = cv2.VideoWriter(videoPath, fourcc, fps, (w, h))
    for im_name in range(len(images)):
        frame = cv2.imread(imgPath + images[im_name])  # 这里的路径只能是英文路径
        # frame = cv2.imdecode(np.fromfile((imgPath + images[im_name]), dtype=np.uint8), 1)  # 此句话的路径可以为中文路径
        print(im_name)
        videoWriter.write(frame)
    print("图片转视频结束！")
    videoWriter.release()
    cv2.destroyAllWindows()


def Video2Pic():
    # USER: legacy helper; set paths before use
    videoPath = r'C:\Users\41663\Desktop\video\4c4c33f9a7\rgb.mp4'  # 读取视频路径
    imgPath = "./pics/"  # 保存图片路径

    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    while suc:
        frame_count += 1
        suc, frame = cap.read()
        # cv2.imwrite(imgPath + str(frame_count).zfill(4), frame)
        cv2.imwrite(imgPath + "%d.jpg" % frame_count, frame)
        cv2.waitKey(1)
        print("%d th frame", frame_count)
    cap.release()
    print("视频转图片结束！")


def decode_video(video_path, save_dir, target_num=None):
    '''
    video_path: 待解码的视频
    save_dir: 抽帧图片的保存文件夹
    target_num: 抽帧的数量, 为空则解码全部帧, 默认抽全部帧
    '''

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("can not open the video")
        exit(1)
    count = 0
    index = 1
    frames_num = video.get(7)
    # 如果target_num为空就全部抽帧,不为空就抽target_num帧
    if target_num is None:
        step = 1
        print('all frame num is {}, decode all'.format(int(frames_num)))
    else:
        step = int(frames_num / target_num)
        print('all frame num is {}, decode sample num is {}'.format(int(frames_num), int(target_num)))

    fps = video.get(cv2.CAP_PROP_FPS)

    while True:
        _, frame = video.read()
        if frame is None:
            break
        if index == frames_num and target_num is None:
            # 如果全部抽，抽到所有帧的最后一帧就停止
            break
        elif index == target_num and target_num is not None:
            # 如果采样抽，抽到target_num就停止
            break

        if count % step == 0:
            save_path = "{}/{:>04d}.png".format(save_dir, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
        cv2.waitKey(int(1000 / int(fps)))
    video.release()


def _resolve_rdvs_video(rdvs_dir, vid):
    for ext in (".mp4", ".webm", ".mkv"):
        p = os.path.join(rdvs_dir, vid + ext)
        if os.path.isfile(p):
            return p
    return None


if __name__ == '__main__':
    # Video2Pic()  # 视频转图像
    # Pic2Video() #图像转视频
    base = os.path.dirname(os.path.abspath(__file__))
    # ----- USER: edit paths / list file (see USAGE.txt) -----
    LIST_FILE = "download.txt"  # one video ID per line; file must sit next to this script unless you use an absolute path
    RDVS_DIR = "rdvs"  # folder with <ID>.mp4 / .webm / .mkv
    OUT_BASE = "image"  # frames -> OUT_BASE/<ID>/0001.png, ...
    # ---------------------------------------------------------
    list_path = os.path.join(base, LIST_FILE) if not os.path.isabs(LIST_FILE) else LIST_FILE
    rdvs_dir = os.path.join(base, RDVS_DIR) if not os.path.isabs(RDVS_DIR) else RDVS_DIR
    out_base = os.path.join(base, OUT_BASE) if not os.path.isabs(OUT_BASE) else OUT_BASE
    with open(list_path, "r", encoding="utf-8") as f:
        ids = [line.strip() for line in f if line.strip()]
    for vid in ids:
        video_path = _resolve_rdvs_video(rdvs_dir, vid)
        if video_path is None:
            print("can not open the video: no file for %s in %s" % (vid, rdvs_dir))
            continue
        save_dir = os.path.join(out_base, vid)
        decode_video(video_path, save_dir)
