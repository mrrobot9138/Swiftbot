# Swiftbot
A question-answer chatbot using the Langchain framework. You have the flexibility to choose any embedding and language model of your preference. The chatbot should be able to answer questions based on the thesis: Celebrity, Music, and Public Persona: A Case Study of Taylor Swift. Using Vector Database "Pinecone".

Note it is a assignment completed as quick as possible due to some constraints and the initial runthrough on data will take a little tile as the data give is large
And have not properly documented the code such as comments etc 

Features
Question-Answering: Users can ask questions about Taylor Swift's life, career, or any related topic.
Document Retrieval: The chatbot retrieves relevant documents from a database based on the user's question.
Natural Language Processing: The chatbot uses advanced language processing techniques to understand and respond to user queries.
How it Works
Input: Users type their question in the text input field provided.
Processing: When the user clicks the "Ask" button, the chatbot processes the question using advanced language processing techniques.
Document Retrieval: The chatbot searches through a database of documents related to Taylor Swift and retrieves the most relevant ones based on the user's question.
Answer Generation: The chatbot analyzes the retrieved documents to find the best answer to the user's question.
Output: The chatbot displays the answer to the user in the interface.
Usage
Installation:

Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Running the Chatbot:

Navigate to the project directory in your terminal.
Run the command streamlit run chatbot.py to start the application.
Access the chatbot interface in your web browser.
Asking Questions:

Type your question in the text input field provided.
Click the "Ask" button to submit your question.
The chatbot will process your question and display the answer on the screen.
Technologies Used
Streamlit: The user interface of the chatbot is built using Streamlit, a Python library for creating interactive web applications.
Pinecone: Pinecone is used for creating and querying the database of documents related to Taylor Swift.
Sentence Transformers: Sentence Transformers is used for generating embeddings of user questions and documents, enabling semantic similarity comparison.
Langchain: Langchain provides various NLP functionalities, including document loading, text splitting, and question-answering capabilities.
Future Improvements
Implement more advanced NLP techniques for better question understanding and answer generation.
Expand the database of documents to cover a wider range of topics related to Taylor Swift.
Improve the user interface for a more intuitive and engaging experience.
