import cv2
import requests
import numpy as np

THRESHOLD=[0,32,64,96,128,160,191,224]
CHARACTER=['.',',',':',';','=','+','*','#']
CHARACTER_FILLED = [' ', '░', '▒', '▓', '█', '█', '█', '█']

def read_img(img_path):
    image=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    return image

def resize_img(image,window_height,window_width):
    window_asp_ratio=window_width/window_height
    img_asp_ratio=image.shape[1]/image.shape[0]
    if window_asp_ratio>img_asp_ratio:
        #Image is taller than the window
        new_width=int(window_height*img_asp_ratio)-1
        new_height=window_height-1
    elif window_asp_ratio<img_asp_ratio:
        new_height=int(window_width/img_asp_ratio)-1
        new_width=window_width-1
    else:
        new_height=window_height-1
        new_width=window_width-1
    resized_img=cv2.resize(image,(new_width,new_height))
    return resized_img

def pixel_to_char(pixel_intensity,mode):
    index=-1
    for i in range(len(THRESHOLD)):
        if pixel_intensity>=THRESHOLD[i]:
            index+=1
        else:
            break
    if index==-1:
        return ""
    else:
        if mode=="normal":
            return CHARACTER[index]
        else:
             return CHARACTER_FILLED[index]

def img_to_ascii(image,mode):
    output=""
    for row in image:
        for pixel_intensity in row:
            output+=pixel_to_char(pixel_intensity,mode)
        output+="\n"
    
    output_list=list(output.split("\n"))
    return output_list

def get_img_from_url(url,color):
    response = requests.get(url)
    image_data = response.content
    image_array = np.frombuffer(image_data, np.uint8)
    if color==1:
        image = cv2.imdecode(image_array,cv2.IMREAD_COLOR)
    else:
        image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    return image
