from curses import wrapper
from moviepy.editor import VideoFileClip
import pygame
import time
import cv2

from utils.image_utils import read_img,resize_img,img_to_ascii,pixel_to_char

class VideoPlayer():
    def __init__(self):
        pass

    def play_video(self,home_screen):
        def main(stdscr):
            video_path=self.video_path

            video=cv2.VideoCapture(video_path)
            stdscr.nodelay(True)

            video_clip = VideoFileClip(video_path)
            audio = video_clip.audio
            audio_path = "extracted_audio.wav"
            audio.write_audiofile(audio_path)

            pygame.mixer.init()
            sound = pygame.mixer.Sound(audio_path)

            tm1=time.time()
            start_time=time.time()
            frames=0
            fps=0
            target_fps=video.get(cv2.CAP_PROP_FPS)
            delay=1/target_fps
            sound.play()
            while True:
                ret,frame=video.read()
                window_height, window_width = stdscr.getmaxyx()
                if ret==True:
                    frames+=1
                    tm2=time.time()
                    if(tm2-tm1!=0):
                        fps=frames/(tm2-tm1)
                    stdscr.clear()
                    image=frame
                    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    resized_img=resize_img(gray,window_height,window_width)
                    ascii_art=img_to_ascii(resized_img,mode=self.mode)
                    display_x_start=(window_width-resized_img.shape[1])//2
                    display_y_start=(window_height-resized_img.shape[0])//2
                    j=display_y_start
                    stdscr.addstr(0,window_width-len("[H]ome")-2,"[H]ome")
                    for row in ascii_art:
                        for i in range(display_x_start,len(row)+display_x_start):
                            stdscr.addstr(j,i,row[i-display_x_start])
                        j+=1
                    current_time=time.time()
                    elapsed_time=current_time-start_time
                    target_time=frames*delay
                    if elapsed_time<target_time:
                        time.sleep(target_time-elapsed_time)
                    elif elapsed_time>target_time:
                        time.sleep(0)             
                    stdscr.refresh()
                    try:
                        key=stdscr.getkey()
                    except:
                        key=None
                    if key =="h":
                        sound.stop()
                        stdscr.clear()
                        break
                else:
                    break


        wrapper(main)
        home_screen.active=True
        home_screen.create_logo()
        home_screen.display_home_screen(video_player=self)