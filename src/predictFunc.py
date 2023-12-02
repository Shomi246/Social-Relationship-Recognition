from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array, array_to_img, load_img, to_categorical
import numpy as np

model_path = './src/social_relation_detection_model/pcvt.h5'
# model_path = './social_relation_detection_model/pcvt.h5'

model_pred = load_model(model_path, compile=False)

def decodeResult(prd_result):
    rltn_result = []
    for val in prd_result:
        if (val==0):
            rltn_result.append("Friend")
        elif (val==1):
            rltn_result.append("Family Member")
        elif (val==2):
            rltn_result.append("Couple")
        elif (val==3):
            rltn_result.append("Professional")
        elif (val==4):
            rltn_result.append("Commercial")
        elif (val==5):
            rltn_result.append("No Relation")
        else:
            rltn_result.append("Not detected")

    return rltn_result
        

def predictRelation(numOfPair):
    imgs_pred  = [i for i in range(1, numOfPair+1)]
    data_x = []
    for val in imgs_pred:
        # img = load_img("../static/temp_img/"+str(val)+".jpg", target_size=(224, 224))  
        img = load_img("static/temp_img/"+str(val)+".jpg", target_size=(224, 224))  
        x = img_to_array(img)
        x = (x ) / 255.0
        data_x.append(x)
    data_x = np.array(data_x)

    # predict relationship with ml model
    y_pred = model_pred.predict(data_x)
    prd_result = np.array(np.apply_along_axis(np.argmax, axis=1, arr=y_pred))
    rltn_result = decodeResult(prd_result)
    return rltn_result
