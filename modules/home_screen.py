import cv2
import rich
from rich.console import Console
import os

from utils.image_utils import read_img,resize_img,img_to_ascii,pixel_to_char,get_img_from_url
from utils.os_utils import clear_screen

class HomeScreen:
    def __init__(self):
        self.active=True #When active then display the home screen
        self.close_app=False
        self.console=Console()
    
    def create_logo(self):
        url_1 = 'https://i.pinimg.com/736x/24/45/55/24455595dc4a2ed5127813ae665c7253.jpg'
        url_2='https://i.pinimg.com/originals/ba/ec/1f/baec1f8c741adf21ce2c53a77fcf7e12.png'
        image=get_img_from_url(url_1,color=0)
        resized_img=cv2.resize(image,(self.console.width,self.console.height-5))
        ascii_art=img_to_ascii(resized_img,mode="filled")

        colored_img=get_img_from_url(url_2,color=1)
        resized_img_colored=cv2.resize(colored_img,(self.console.width,self.console.height-5))

        self.logo=rich.text.Text("")

        i=0

        for row in ascii_art:
            for j in range(0,len(row)):
                text=rich.text.Text(row[j])
                text.stylize(f"rgb({resized_img_colored[i][j][2]},{resized_img_colored[i][j][1]},{resized_img_colored[i][j][0]})")
                self.logo+=text
            i+=1
            self.logo+=rich.text.Text("\n")
        
    def display_home_screen(self,video_player):
        while self.active==True:
            clear_screen()
            self.console.print(self.logo,justify="center")
            slogan=rich.text.Text("Reimagining Video: ASCII Art in Your Terminal")
            slogan.stylize("rgb(185,105,209)")
            self.console.print("\n")
            self.console.print(slogan,justify="center")
            self.console.print("\n")
            self.console.print("\n")
            
            exit=self.console.input("Enter 'quit' if you want to quit, otherwise type anything and press enter ")
            if exit.strip().lower()=="quit":
                self.close_app=True
                break

            video_exists=False
            while video_exists==False:
                video_path=self.console.input("Enter video path(preferably mp4 format) ")
                if os.path.exists(video_path):
                    if video_path.endswith(".mp4"):
                        video_exists=True
                        video_player.video_path=video_path
                    else:
                        clear_screen()
                        self.console.print(self.logo,justify="center")
                        slogan=rich.text.Text("Reimagining Video: ASCII Art in Your Terminal")
                        slogan.stylize("rgb(185,105,209)")
                        self.console.print("\n")
                        self.console.print(slogan,justify="center")
                        self.console.print("\n")
                        self.console.print("\n")
                        self.console.print("enter file of mp4 format.")
                else:
                    clear_screen()
                    self.console.print(self.logo,justify="center")
                    slogan=rich.text.Text("Reimagining Video: ASCII Art in Your Terminal")
                    slogan.stylize("rgb(185,105,209)")
                    self.console.print("\n")
                    self.console.print(slogan,justify="center")
                    self.console.print("\n")
                    self.console.print("\n")
                    self.console.print("Invalid path. Please try again.")
            correct_mode=False
            while correct_mode==False:
                mode=self.console.input("Enter mode (normal/filled) ")
                if mode.strip().lower()=="normal" or mode.strip().lower()=="filled":
                    correct_mode=True
                    video_player.mode=mode
                else:
                    clear_screen()
                    self.console.print(self.logo,justify="center")
                    slogan=rich.text.Text("Reimagining Video: ASCII Art in Your Terminal")
                    slogan.stylize("rgb(185,105,209)")
                    self.console.print("\n")
                    self.console.print(slogan,justify="center")
                    self.console.print("\n")
                    self.console.print("\n")
                    self.console.print("Enter a valid mode.")

            clear_screen()
            self.active=False
        
        if self.close_app==False:
            video_player.play_video(home_screen=self)
        else:
            clear_screen()
        

            