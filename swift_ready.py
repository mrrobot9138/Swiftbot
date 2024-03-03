import streamlit as st
import pinecone
import os
from sentence_transformers import SentenceTransformer
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain

# Load environment variables
load_dotenv()

# Load Sentence Transformers model
sentence_model = SentenceTransformer('paraphrase-distilroberta-base-v2')

# Initialize Pinecone client
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment="gcp-starter"
)

# Function to read documents
def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    return documents

# Function to chunk data
def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    doc = text_splitter.split_documents(docs)
    return docs

# Load documents and chunk data
documents = chunk_data(docs=read_doc('documents/'))

# Initialize Pinecone index
index_name = "langchainvector"
index = Pinecone.from_documents(documents, index_name=index_name)

# Load Q&A chain
chain = load_qa_chain(llm=None, chain_type="stuff")

# Function to retrieve answers
def retrieve_answers(user_question_embedding):
    # Search for similar embeddings in Pinecone
    results = index.similarity_search(user_question_embedding, k=1)
    if results:
        document_id = results[0].id
        # Run Q&A chain to get answer
        answer = chain.run(input_documents=[document_id], question=user_question)
        return answer
    else:
        return "No matching document found."

# Streamlit UI
st.title("Taylor Swift Chatbot")

# User input
user_question = st.text_input("Ask a question")

# Get response on button click
if st.button("Ask"):
    if user_question:
        # Get embeddings for the user question
        user_question_embedding = sentence_model.encode([user_question])[0]
        
        # Retrieve answer
        answer = retrieve_answers(user_question_embedding)
        
        # Display the answer
        st.text("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")