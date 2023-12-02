# Web Application Enhanced Image Captioning Implies Social Relationships

The proposed CvT based system is an innovative web application that combines advanced techniques in computer vision and natural language processing to detect social relationships in images and enhance image captions accordingly.

## System Architecture

This system integrates a frontend and backend component to provide a seamless user experience.

![Diagram of System Architecture](images/System_Architecture.png)

### Frontend Component
A responsive website allowing users to:

- Upload images for analysis.
- View the annotated images with predicted social relationships.
- See enhanced image captions that integrate the predicted relationships.

### Backend Component
Comprises several modules, including:

- **Pretrained Annotation Model**: Annotates images using a pre-trained model to locate people and provide bounding box coordinates.
- **Pair Combination Module**: Creates pairs of individuals from the image to prepare for relationship prediction.
- **Convolutional Vision Transformer (CvT) Based Classifier**: Predicts the social relationship between paired individuals.
- **Image Captioning Module**: Enhances the original image caption by incorporating the predicted social relationships.

## Web Application Development
<img src="images/web_app_1.png" alt="Upload an image" width="300"/> <!-- Adjust width as needed -->
<img src="images/web_app_2.png" alt="Annotated image" width="300"/> <!-- Adjust width as needed -->
<img src="images/web_app_3.png" alt="Cropped images" width="300"/> <!-- Adjust width as needed -->
![Relationship Prediction and Pairwise Caption](images/web_app_4.png)
![Enhanced Image Caption](images/web_app_5.png)

The web application is developed using Python and the following frameworks and libraries:

- **Jinja**: For dynamic HTML templating.
- **Bootstrap**: For designing a responsive user interface.
- **Flask**: As the web framework for route management and server-side logic.

## Python Libraries Used

- **Numpy**: For numerical computing and array manipulation.
- **OS**: For interacting with the operating system.
- **NLTK**: For natural language processing tasks.
- ... (continue with the rest of the libraries as in your draft)

## Installation

1. Clone the repository and switch to the `main` branch:
   ```bash
   git clone https://github.com/Shomi246/Social-Relationship-Recognition.git
   cd Social-Relationship-Recognition
   git checkout main

2. Create and activate the Anaconda environment using the ESetup.yaml file:
   ```bash
   conda env create -f ESetup.yaml
   conda activate SRRC-CvT-env

4. Start the web application server:
   ```bash
   ./runserver.sh
