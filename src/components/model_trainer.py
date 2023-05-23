import numpy as np
from keras.models import load_model
import pandas as pd
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def output():
    # img=cv2.imread("src\predicted_images\source.jpeg")
    # cv2.imshow("original_image",img)
    # cv2.waitKey(0)
    image = mpimg.imread("src\predicted_images\source.jpeg")
    plt.title("original_image")
    plt.imshow(image)
    plt.show()
    images=["src\predicted_images\photo1.png","src\predicted_images\photo2.png","src\predicted_images\photo3.jpg","src\predicted_images\photo4.jpg","src\predicted_images\photo5.jpg"]
    for i in images:
        # img=cv2.imread(i)
        # cv2.imshow("predictions" ,img)
        image = mpimg.imread(i)
        plt.title("predicted_image")
        plt.imshow(image)
        plt.show()
        
    

