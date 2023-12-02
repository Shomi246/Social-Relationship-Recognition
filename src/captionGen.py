import spacy
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

modelv = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelv.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_paths):
  images = []
  for image_path in image_paths:
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = modelv.generate(pixel_values, **gen_kwargs)#

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  return preds


nlp = spacy.load("en_core_web_sm")

def predictCaptionPair(imagePath, plab1):

    imgpaths= "static/temp_img/"+str(imagePath)+".jpg"
    # imgpaths= "../static/temp_img/"+str(imagePath)+".jpg"

    # Input predicted caption and predicted class
    predicted_captions = predict_step([imgpaths]) # Get predicted captions as a list
    predicted_caption = predicted_captions[0] # Extract the first predicted caption
    # predicted_class = plab 

    # Process the predicted caption with spaCy
    doc = nlp(predicted_caption)

    # Find the subject of the predicted caption using Named Entity Recognition (NER)
    subject = None
    for ent in doc.ents:
        if ent.label_ == "PERSON" or ent.label_ == "NORP":
            subject = ent
            break
    # If subject not found using NER, try dependency parsing
    if not subject:
        for token in doc:
            if "subj" in token.dep_:
                subject = token
                break
    # Find all the subjects in the predicted caption
    subjects = []
    for token in doc:
        if token.pos_ == "NOUN" and "subj" in token.dep_:
            subjects.append(token)

    # Replace the first subject with the predicted class and the rest of the subjects with null value
    new_caption = predicted_caption
    # new_caption = new_caption.replace("couple ", "")

    # for i, subject in enumerate(subjects):
    #     if i == 0:
    #         # Replace the first subject with the predicted class
    #         if plab1 == "Friend":
    #             predicted_class = "friends "
    #         elif plab1 == "Family Member":
    #             predicted_class = "family members "
    #         elif plab1 == "Couple":
    #             predicted_class = "couple "
    #             new_caption = new_caption.replace("two", "a", 1)
    #         elif plab1 == "Professional":
    #             predicted_class = "professional people "
    #             # predicted_class = "two professional people"
    #         elif plab1 == "Commercial":
    #             predicted_class = "commercial people "
    #         elif plab1 == "No Relation":
    #             predicted_class = "people they have no relation "
    #         new_caption = new_caption.replace(subject.text, predicted_class, 1)
    #     else:
    #         # Replace the rest of the subjects with null value
    #         new_caption = new_caption.replace(subject.text, "")

    # if(len(subjects)==0):
    if plab1 == "Friend":
        predicted_class = "they are friends"
    elif plab1 == "Family Member":
        predicted_class = "they are family members"
    elif plab1 == "Couple":
        predicted_class = "they are couple"
        # new_caption = new_caption.replace("two", "a", 1)
    elif plab1 == "Professional":
        predicted_class = "they are professional people"
            # predicted_class = "two professional people"
    elif plab1 == "Commercial":
        predicted_class = "they are commercial people"
    elif plab1 == "No Relation":
        predicted_class = "they have no relation"
    new_caption = f"{new_caption} and {predicted_class}"#predicted_class+new_caption#.replace(subject.text, predicted_class, 1)

    predicted_caption1=new_caption+"."

    return predicted_caption1

#new
def generateSingleCaption(img_path):
    img_cap = predict_step([img_path])
    #generate caption for whole image
    img_cap = img_cap[0]
    return img_cap



# predictCaptionPair('../static/temp_img/1.jpg', 3)