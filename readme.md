# Farmly (Your Friend In Need)  
### Over View :-   
- We have used Django for our mini project, Which is python library used for web developmnet.  
- In this particular project we provide the input to the model using UI and the disease realted to sugarcane is displayed to the user in the UI.  
### How this functionality is achieved.  
- First we have provided the UI through which farmer can upload the image of crop(Sugarcane), which is developed using HTML5, CSS & Javascript along with some libraries like bootstrap and jquery.   
- Next when your image get's uploaded the button(Diagnose crop) becomes active.  
- 3)When you click on diagnose button it will send image to model for processing.  
- 4)Once model finishes the processing it will output the result as name of disease or healthy crop on the UI.  


## Technologies Used :
- 1)Tensorflow  
- 2)Django  
- 3)Computer Vision  
- 4)Open CV  
- 4)Pandas   

### Steps to run this project locally : 
**Installation**
1) Install python version 3.9.7 or greater
2) Install django version 
3) pip install -r requirements.txt
4) If there is pip version error upgrade the pip using commmand ( python -m pip install --upgrade pip)
5) Navigate to HealtyCrop and find manage.py.
6) Hit the command python manage.py runserver at CLI
7) If every thing is right open your browser and hit 127.0.0.1:8000
8) You will see the Farmly home screen.

