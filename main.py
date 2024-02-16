import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -stream_loop -1 -re -i video.mp4 -stream_loop -1 -re -i *audio file* -vcodec libx264 -pix_fmt yuvj420p -maxrate 2048k -preset ultrafast -r 12 -framerate 1 -g 50 -crf 51 -c:a aac -b:a 128k -ar 44100 -strict experimental -video_track_timescale 100 -b:v 500k -f flv  rtmp://a.rtmp.youtube.com/live2/stxx-acpv-mz3b-m02a-2e9r')