from keras.models import load_model 
from src.exception import CustomException
from src.logger import logging
from PIL import Image
from src.components.model_trainer import output
import numpy as np



def pred(model, img:str):
    mod=load_model(model)
    img=Image.open("")
    img=np.asarray(img)

    return output(img)