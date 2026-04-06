"""
Optional: trim a short clip from a video (needs: pip install moviepy).
"""
from moviepy.editor import VideoFileClip

# ----- USER: input video path, fps-based trim range, output file -----
clip = VideoFileClip(r'./wsvd/SKpiEQIvcxo.webm')
fps = clip.fps
print(fps)
start = 2965 // fps
end = 3011 // fps
video_clip = clip.subclip(start, end)
video_clip.to_videofile('overlooking.mp4')
# --------------------------------------------------------------------