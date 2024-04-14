from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import os 
import cv2
from PIL import Image as Img
import numpy as np 
from django.conf import settings
import datetime
import tensorflow as tf

# from django.core.files.storage import FileSystemStorage

# # Create your views here.

# class CustomFileSystemStorage(FileSystemStorage):
#     def get_available_name(self,)

def index(request):
    return render(request,"index.html")

def result(request):
    if request.method == "POST":
        # first we will process the image and check if it is sugarcane or not.
        #if iamge is not sugarcane we will simply output the result that image is not sugarcane 
        result = process_is_sugarcane(request)

        if result["result"]:
            disease = find_disease(result["path"])
            data ={
                'condition': disease,
                'pathh' : result["name"]
                
            }
            return render(request, "result.html",data)
            # process your actual model 
        else:    
            data = {
                'warning':"Seems like you have not uploaded the image of sugarcane",
                'pathh' : result["name"]
            }
            return render(request, "result.html",data)

    else:
        return HttpResponse("NO worry get out !!")



#writing code to process if the image is of sugarcane or not 

def process_is_sugarcane(request):
    new_name = str(datetime.datetime.now())
    new_name= new_name.replace(" ", "_")
    new_name= new_name.replace(":", "_")
    img = request.FILES.get("image_form")
    img.name = str(new_name + img.name)
    
    i_path = str(settings.MEDIA_ROOT) + "/images/" + img.name
    print(i_path)
    sv = Image(crop_image=img)
    sv.save()
    imag = cv2.imread(i_path)
    print(imag)
    img_from_arr = Img.fromarray(imag,'RGB')
    resized_image = img_from_arr.resize((224,224))
    test_image= np.expand_dims(resized_image, axis=0)
    model = tf.keras.models.load_model(os.getcwd() + "/keras_model.h5")
    result = model.predict(test_image)
    print(result)
    is_sugarcane = True
    if result[0][0] < result[0][1]: 
        print("HEY")
        is_sugarcane = False


    res = {
        'result' : is_sugarcane,
        'path': i_path,
        'name':None
    }
    res["name"] = img.name

    return res
    

#implementing logic to find the disease for sugarcane

def find_disease(path):
    print(path)
    imag = cv2.imread(path)
    img_from_arr = Img.fromarray(imag,'RGB')
    resized_image = img_from_arr.resize((224,224))
    test_image= np.expand_dims(resized_image, axis=0)
    model = tf.keras.models.load_model(os.getcwd() + "/new_keras_model.h5")
    result = model.predict(test_image)
    print(result)
    print(np.argmax(result))

    disease = None

    if np.argmax(result) == 0:
        disease = "Grassy Shoot"
    elif np.argmax(result) == 1:
        disease = "Sugarcane Gumming"
    elif np.argmax(result) == 2:
        disease = "Sugarcane Mosaic"
    elif np.argmax(result) == 3:
        disease = "Sugarcane Rotten Stunting"
    elif np.argmax(result) == 4:
        disease = "Sugarcane red rot"
    elif np.argmax(result) == 5:
        disease = "Sugarcane rusting"
    elif np.argmax(result) == 6:
        disease = "Sett rot or pineapple"
    elif np.argmax(result) == 7:
        disease = "Sumt of sugarcane"
    elif np.argmax(result) == 8:
        disease = "Wilt"
    elif np.argmax(result) == 9:
        disease = "Healthy Sugarcane"

    return disease