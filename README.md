# Echo: Personal Talking Healthcare Chatbot
Echo is an advanced personal healthcare chatbot designed to provide users with responses based on their spoken symptoms. The project combines natural language processing (NLP) techniques with speech recognition and text-to-speech capabilities to create an interactive and user-friendly experience.

**Features**
Voice Interaction: Engage with the chatbot through voice commands, with support for both male and female voices.
Symptom Recognition: The chatbot uses a trained model to interpret and respond to user-reported symptoms.
Dynamic Voice Selection: Users can choose their preferred voice at the start of the interaction.
Continuous Operation: The chatbot continues to interact until the user decides to end the session.

**Training**
The model is trained using a combination of NLP techniques and machine learning algorithms. The training process involves:

Text Preprocessing: Uses NLTK for tokenization and lemmatization of text data.
Model Architecture: A neural network built with TensorFlow and Keras, including layers for dense connections, activation, dropout, and optimization.
Data Handling: Uses JSON and pickle for managing training data and model serialization.

**Testing and Usage**
The chatbot's functionality is tested and deployed using:

Speech Recognition: Converts spoken symptoms into text using Google's speech recognition API.
Text-to-Speech: Provides spoken responses based on the recognized text.
User Interaction: Engages users through voice commands and provides feedback.
