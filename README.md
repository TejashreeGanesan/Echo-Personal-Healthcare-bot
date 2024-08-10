# Echo: Personal Talking Healthcare Chatbot
Echo is an advanced personal healthcare chatbot designed to provide users with responses based on their spoken symptoms. The project combines natural language processing (NLP) techniques with speech recognition and text-to-speech capabilities to create an interactive and user-friendly experience.

## Features

- Voice Interaction: Engage with the chatbot through voice commands, with support for both male and female voices.

- Symptom Recognition: The chatbot uses a trained model to interpret and respond to user-reported symptoms.

- Dynamic Voice Selection: Users can choose their preferred voice at the start of the interaction.

- Continuous Operation: The chatbot continues to interact until the user decides to end the session.

## Training

The model is trained using a combination of NLP techniques and machine learning algorithms. The training process involves:

- Text Preprocessing: Uses NLTK for tokenization and lemmatization of text data.

- Model Architecture: A neural network built with TensorFlow and Keras, including layers for dense connections, activation, dropout, and optimization.

- Data Handling: Uses JSON and pickle for managing training data and model serialization.

## Testing and Usage

The chatbot's functionality is tested and deployed using:

- Speech Recognition: Converts spoken symptoms into text using Google's speech recognition API.

- Text-to-Speech: Provides spoken responses based on the recognized text.

- User Interaction: Engages users through voice commands and provides feedback.

## Installation

### Clone the Repository:
> git clone repository-url

> cd repository-directory

### Install Dependencies:

Make sure you have Python installed, then install the required packages:

> pip install nltk tensorflow keras SpeechRecognition pyttsx3 numpy
### Setup Training and Intents Files:

Ensure that you have intents.json and any other necessary files for training in the project directory.

## Usage

### Train the Model:

Run the training script to build and save the model.

> python train.py
> 
### Run the Chatbot:
Execute the testing script to start the chatbot and interact with it.

> python main.py
### Interact with the Chatbot:

Speak your symptoms to the chatbot.
Choose your preferred voice when prompted.
The chatbot will analyze your symptoms and provide responses based on its training.
### End the Session:
Say "Leave" or any other exit command to stop the chatbot.

## Screenshot

![image](https://github.com/user-attachments/assets/af97fd70-05b8-4a93-9788-b79a1de96924)

