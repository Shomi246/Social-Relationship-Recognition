import openai
openai.api_key = "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" #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"

def summaryGen(sin_cap, caption_list):
    # model = "text-davinci-002"

    # text= "rest of the sentences are the caption of a whole image, based on those captions and relationship describe the image in one sentence with relationship in it in a meaningful way. "

    # Extract relationships from caption_list
    relationship_list = []
    for caption in caption_list:
        if "friends" in caption.lower():
            relationship_list.append("friends")
        elif "family members" in caption.lower():
            relationship_list.append("family members")
        elif "couple" in caption.lower():
            relationship_list.append("couple")
        elif "professional people" in caption.lower():
            relationship_list.append("professional people")
        elif "commercial people" in caption.lower():
            relationship_list.append("commercial people")
        elif "no relationship" in caption.lower():
            relationship_list.append("no relationship")
            
    # Remove duplicates from relationship_list
    relationship_list = list(set(relationship_list))

    # Construct summary
    summary = sin_cap + " "
    if len(relationship_list) == 1:
        summary += "and the relationship is " + relationship_list[0] + ". "
    elif len(relationship_list) > 1:
        summary += "and the relationships are "
        for i in range(len(relationship_list)-1):
            summary += relationship_list[i] + ", "
        summary += "and " + relationship_list[-1] + ". "
    else:
        summary += "and no relationship mentioned. "
        
    # # concatenate document with prompt
    # prompt = summary + text
    # for caption in caption_list:
    #     prompt += caption + " "

    # response = openai.Completion.create(
    #   engine=model,
    #   prompt=prompt,
    #   max_tokens=60,
    #   n=1,
    #   stop=None,
    #   temperature=0.5,
    # )
    # summary = response.choices[0].text.strip()
    return summary



# import openai
# openai.api_key = "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"

# def summaryGen(sin_cap, caption_list):
#     model = "text-davinci-002"

#     text= "rest of the sentences are the caption of a whole image, based on the main caption describe the image in one sentence and from the relationship caption just take the relationship and include those relationship to the description in a meaningful way. The main caption is:"
    
#     # create the document string
#     # document = " ".join(sin_cap) + " " + text 
#     document = " ".join(text + sin_cap) + "."+"the relationship caption are:"

#     # document = " ".join(sin_cap) + " " 
#     for caption in caption_list:
#         document = document + caption + " "
    
#     # concatenate document with prompt
#     prompt = document #+ " ".join(caption_list)
#     # model = "text-davinci-002"
#     # prompt = " ".join([sin_cap]+caption_list)  # Join the caption list into a single string
#     response = openai.Completion.create(
#       engine=model,
#       prompt=prompt,
#       max_tokens=60,
#       n=1,
#       stop=None,
#       temperature=0.5,
#     )
#     summary = response.choices[0].text.strip()
#     return summary

# import openai
# openai.api_key = "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"

def summaryGen1(sin_cap, caption_list):
    
    if caption_list.count(".") <= 6:
      model = "text-curie-001"
    else:
      model = "text-davinci-003"
        
    # text= "rest of the sentences are the caption of a whole image, based on those captions and relationship describe the image in one sentence with relationship in it in a meaningful way. "
    # text= "below are the caption of a whole image, describe and summarize the all caption of the image using only one line based on the 1st paragraph sentence and Include the mentioned relationship on it in a meaningful way with correct semantics."
    text= "below are the caption of a whole image, summarize the caption of the image using just in one sentence based on the 1st paragraph sentence and all the mentioned relationship from the 2nd paragraph on it in a meaningful way and in one sentence and one line only never mention image1, image2, image3."

    # create the document string
    document = text + "\n\n" + " ".join(sin_cap) + "."+"\n" 
    for caption in caption_list:
        document = document + caption + " "
    # document = " ".join(text + sin_cap) + " "
    # for caption in caption_list:
    #     document = document + caption + " "
    
    # concatenate document with prompt
    prompt = document
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.5,
    )
    summary1 = response.choices[0].text.strip()
    return summary1

def summaryGen3(sin_cap):
    
  
    model = "text-curie-001"
   
        
    # text= "rest of the sentences are the caption of a whole image, based on those captions and relationship describe the image in one sentence with relationship in it in a meaningful way. "
    # text= "below are the caption of a whole image, describe and summarize the all caption of the image using only one line based on the 1st paragraph sentence and Include the mentioned relationship on it in a meaningful way with correct semantics."
    text= "below are the caption of a whole image, summarize the caption of the image using just in one sentence and all mentioned relationship in a meaningful way."

    # create the document string
    document = text + "\n\n" + " ".join(sin_cap) 
    
    # concatenate document with prompt
    prompt = document
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.5,
    )
    summary2 = response.choices[0].text.strip()
    return summary2

# def generate_enhanced_summary(summary, summary1, summary2):
#     prompt = f"Generate an enhanced summary based on the following three summaries:\n\n{summary}\n\n{summary1}\n\n{summary2}\n\nEnhanced summary:"
#     model = "text-davinci-002"
#     response = openai.Completion.create(
#         engine=model,
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=256,
#         n=1,
#         stop=None,
#         timeout=60,
#     )
#     enhanced_summary = response.choices[0].text.strip()
#     return enhanced_summary

def generate_enhanced_summary(summary):
    prompt = f"Generate an enhanced summary based on the following line:\n\n{summary}\n\nEnhanced summary:"
    model = "text-davinci-002"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        n=1,
        stop=None,
        timeout=60,
    )
    enhanced_summary = response.choices[0].text.strip()
    return enhanced_summary

# import openai

# openai.api_key = "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"

# def summaryGen(sin_cap, caption_list):
#     # if caption_list.count(".") <= 6:
#     #     model = "text-curie-001"
#     # else:
#     model = "text-ada-001"
        
#     text= "below are the caption of a whole image, summarize the caption of the image using just in one sentence based on the 1st paragraph sentence and include the relationship from the 2nd paragraph only in it in a meaningful way and in one sentence and one line only."

#     # create the document string
#     document = text + "\n\n" + " ".join(sin_cap) + "."+"\n" 
#     for caption in caption_list:
#         document = document + caption + " "
    
#     # concatenate document with prompt
#     prompt = document
#     response = openai.Completion.create(
#       engine=model,
#       prompt=prompt,
#       max_tokens=60,
#       n=1,
#       stop=None,
#       temperature=0.5,
#     )
#     summary = response.choices[0].text.strip()
#     return summary


# import torch
# from transformers import T5Tokenizer, T5ForConditionalGeneration

# def summaryGen(sin_cap, captionList):
#     # Load T5 tokenizer and model
#     tokenizer = T5Tokenizer.from_pretrained('t5-small')
#     model = T5ForConditionalGeneration.from_pretrained('t5-small')

#     # Concatenate all the captions into a single string
#     caption_text = " ".join(captionList)

#     # Tokenize and encode the input text
#     inputs = tokenizer.encode("summarize: " + caption_text, return_tensors='pt')

#     # Generate summary text
#     outputs = model.generate(inputs, max_length=30, num_beams=4, length_penalty=2.0, early_stopping=True)
#     summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     return summary
# import openai

# openai.ap

#import openai

# openai.api_key = "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"

# def summaryGen(sin_cap, caption_list):
#     # Choose the appropriate model based on the length of the caption list
#     # model = "text-ada-001"
#     # if caption_list.count(".") <= 6:
#     model = "text-curie-001"

#     # Extract relationship terms from caption list
#     relationship_terms = ["friends", "family members", "couple", "professional", "commercial", "no relationship"]
#     caption_relationships = []
#     for caption in caption_list:
#         caption_words = caption.split()
#         caption_relationship = [word for word in caption_words if word in relationship_terms]
#         caption_relationships.extend(caption_relationship)

#     # Remove duplicates from the list of relationships
#     relationships = list(set(caption_relationships))

#     # Create the summary string
#     summary = f"{sin_cap}. "
#     if relationships:
#         if len(relationships) == 1:
#             summary += f"They appeared to be {relationships[0]}."
#         else:
#             summary += "They appeared to be "
#             for i, relationship in enumerate(relationships):
#                 if i == len(relationships) - 1:
#                     summary += f"and {relationship}."
#                 else:
#                     summary += f"{relationship}, "
#     else:
#         summary += "No relationship was apparent."

#     # Generate the summary using OpenAI API
#     prompt = f"Below are the captions of a whole image. Summarize the caption of the image using just one sentence based on the first paragraph sentence, including the relationship from the caption list in a meaningful way:\n\n{sin_cap}.\n\nRelationships: {', '.join(relationships)}"
#     response = openai.Completion.create(
#         engine=model,
#         prompt=prompt,
#         max_tokens=60,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     summary += " " + response.choices[0].text.strip() + "."

#     return summary


