# @author: Shahana Shultana
# @copyright: All rights are reserved by author

from flask import Flask, request, render_template
import numpy as np
import os

# custom libraries
from src.imageCropper import bboxAnnotaion, imgprocessor, pairMaker
from src.predictFunc import predictRelation
from src.funcHelper import *
from src.captionGen import predictCaptionPair, generateSingleCaption
from src.summaryGen import summaryGen, summaryGen3, generate_enhanced_summary, summaryGen1

app = Flask(__name__)


@app.route("/")
def homepage():
    data = {'isImagefile': False}
    return render_template('index.html', data=data)


@app.route("/predict", methods=['POST'])
def predict():
    image_file = request.files['image']
    image_filename = image_file.filename
    image_file.save('static/images/' + image_filename)

    # define bbox and annotation
    bbox_info = bboxAnnotaion(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images', image_filename))
    
    # check if there is only one bbox in the image
    if len(bbox_info) < 2:
        data = {'isImagefile': False, 'errorMsg': 'No pair found (only one annotated person) <br>Upload with a different Photo'}
        return render_template('index.html', data=data)

    numOfPair, pairData = pairOrganizer(pairMaker(len(bbox_info)))
    
    imgprocessor('static/images/' + image_filename, len(bbox_info), bbox_info, 1)

    # predict relations
    rltn_predicts = predictRelation(numOfPair)

    # captioning backend
    captionList = []
    indx = 1
    for rltn in rltn_predicts:
        captionList.append(predictCaptionPair(indx, rltn))
        indx+=1

    sin_cap = generateSingleCaption('static/images/' + image_filename)
    # summary generating
    summary = summaryGen(sin_cap, captionList)#, sin_cap)
    summary1 = summaryGen1(summary, captionList)
    summary2 = summaryGen3(summary)

    esum = generate_enhanced_summary(summary) #, summary1, summary2)

    data = {'fileName': image_filename, 'isImagefile': True, 'numOfperson': len(bbox_info), 'numOfPair': numOfPair, 'pairInfo': pairData, 'rltnPredicts': rltn_predicts, 'captions': captionList, 'summary': summary, 'sin_cap': sin_cap, 'summary1': summary1, 'summary2': summary2, 'esum': esum}
    return render_template('index.html', data=data)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)