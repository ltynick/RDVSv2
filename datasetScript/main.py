"""
Optional demo: blend depth and RGB previews (local paths).
NOT needed for video -> frames -> left-half RGB (see USAGE.txt).
"""
import cv2
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # ----- USER: optional; only if you use this depth visualization -----
    src1 = cv2.imread(r"G:\newDataset\boxing_03\depth\10520.png")
    # src2 = cv2.imread(r"G:\newDataset\boxing_03\rgb\10520.png")
    src2 = cv2.imread(r"F:\RAFT-depth\right\10520.png")
    # --------------------------------------------------------------------
    c = cv2.addWeighted(src2, 0.7, src1, 0.3, 0)

    cv2.imshow("addWeighted", c)

    cv2.waitKey(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
