import cv2
import tensorflow as tf
import numpy as np
import pandas as pd
import os

import warnings
warnings.filterwarnings("ignore")

model_path = './src/faster_rcnn_resnet101_v1_1024x1024_coco17_tpu-8/saved_model'
# model_path = './faster_rcnn_resnet101_v1_1024x1024_coco17_tpu-8/saved_model'
detect_fn = tf.saved_model.load(model_path)

def bboxAnnotaion(image_path):
    image = cv2.imread(image_path)

    # Convert the image to RGB
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to a tensor and pass it through the model
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = detect_fn(input_tensor)

    # Extract information about detected objects
    boxes = detections['detection_boxes'][0].numpy()
    scores = detections['detection_scores'][0].numpy()
    classes = detections['detection_classes'][0].numpy().astype(np.int32)

    # Filter out non-person objects and apply non-maximum suppression
    person_boxes = []
    person_scores = []
    for i in range(len(scores)):
        if classes[i] == 1 and scores[i] > 0.5:
            person_boxes.append(boxes[i])
            person_scores.append(scores[i])
    person_boxes = np.array(person_boxes)
    indices = cv2.dnn.NMSBoxes(person_boxes, person_scores, 0.5, 0.4)
    
    # # Draw bounding boxes around persons
    bbox_info = []
    for i in indices:

        box = person_boxes[i]
        left = int(box[1] * image.shape[1])
        top = int(box[0] * image.shape[0])
        right = int(box[3] * image.shape[1])
        bottom = int(box[2] * image.shape[0])
        bbox_info.append([left, top, right, bottom])
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imwrite("static/temp_img/annoted_image.jpg", image)

    return bbox_info



def pairMaker(numOfppl):
    test_list = []
    for i in range(1, numOfppl+1):
        test_list.append(i)
        
    res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]
    return res

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    if(h==0):
        h=1

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def imgprocessor(img_path, numOfp, bbox, nextId):
  
    img = cv2.imread(img_path)
    immgs = []
    _ids = 1
    for index, boxCord in enumerate(bbox):
#         print(index+1, boxCord, savePath)
        crop_img = img[boxCord[1]:boxCord[3], boxCord[0]:boxCord[2]]
        immgs.append(crop_img)
        cv2.imwrite("static/temp_img/_"+str(_ids)+".jpg", crop_img)
        _ids+=1

    pairCode = pairMaker(numOfp)
    df_ne_an = pd.DataFrame() #dataframe new
    for pair in pairCode:
        img1_ = immgs[list(pair)[0]-1]
        img2_ = immgs[list(pair)[1]-1]

        height1, width1 = img1_.shape[0],img1_.shape[1]
        height2, width2 = img2_.shape[0],img2_.shape[1]
        min_height = max(height1, height2)
#         min_width = min(width1, width2)
        img1_ = image_resize(img1_, height = min_height)
        img2_ = image_resize(img2_, height = min_height)
        im_v = cv2.hconcat([img1_, img2_])
#         print(nextId)
        cv2.imwrite("static/temp_img/"+str(nextId)+".jpg", im_v)
        nextId+=1
    return nextId

# print("Bbox: ", bboxAnnotaion("../static/images/00000.jpg"))

# imgprocessor("../static/images/00000.jpg", len([[30, 250, 361, 640], [195, 226, 535, 638]]), [[30, 250, 361, 640], [195, 226, 535, 638]], 1)


