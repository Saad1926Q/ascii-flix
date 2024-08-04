import cv2
import rich
from rich.console import Console
import os

from utils.image_utils import read_img,resize_img,img_to_ascii,pixel_to_char

class HomeScreen:
    def __init__(self):
        self.active=True #When active then display the home screen
        self.console=Console()
        self.create_logo()
        self.display_home_screen()
    
    def create_logo(self):
        image=read_img('ascii_flix_logo_cropped.png')
        resized_img=cv2.resize(image,(100,60))
        ascii_art=img_to_ascii(resized_img)

        colored_img=cv2.imread('ascii_flix_logo_cropped_02.png')
        resized_img_colored=cv2.resize(colored_img,(100,60))

        self.logo=rich.text.Text("")

        i=0

        for row in ascii_art:
            for j in range(0,len(row)):
                text=rich.text.Text(row[j])
                text.stylize(f"rgb({resized_img_colored[i][j][2]},{resized_img_colored[i][j][1]},{resized_img_colored[i][j][0]})")
                self.logo+=text
            i+=1
            self.logo+=rich.text.Text("\n")
        
    def display_home_screen(self):
        while self.active==True:
            os.system('cls')
            self.console.print(self.logo,justify="center")
            slogan=rich.text.Text("Reimagining Video: ASCII Art in Your Terminal")
            slogan.stylize("rgb(185,105,209)")
            self.console.print("\n")
            self.console.print(slogan,justify="center")
            self.console.print("\n")
            self.console.print("\n")
            input=self.console.input("Type 'start' to continue ")

            if(input=="start"):
                os.system('cls')
                self.active=False