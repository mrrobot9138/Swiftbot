import streamlit as st
import os
import pinecone 
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
load_dotenv()
def read_doc(directory):
    file_loader=PyPDFDirectoryLoader(directory)
    documents=file_loader.load()
    return documents
doc=read_doc('documents/')
len(doc)
def chunk_data(docs,chunk_size=800,chunk_overlap=50):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_documents(docs)
    return docs
documents=chunk_data(docs=doc)
len(documents)
embeddings=OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
embeddings
vectors=embeddings.embed_query("How has Taylor Swift’s presented public persona evolved comparatively throughout the early and late stages of her career?")
len(vectors)
pinecone.init(
    api_key="3291bbcb-ba93-4dfd-aff5-74f88de75246",
    environment="gcp-starter"
)
index_name="langchainvector"
index=Pinecone.from_documents(doc,embeddings,index_name=index_name)
def retrieve_query(query,k=2):
    matching_results=index.similarity_search(query,k=k)
    return matching_results
llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
chain=load_qa_chain(llm,chain_type="stuff")
def retrieve_answers(query):
    doc_search=retrieve_query(query)
    print(doc_search)
    response=chain.run(input_documents=doc_search,question=query)
    return response
our_query = "How has Taylor Swift’s presented public persona evolved comparatively throughout the early and late stages of her career?"
answer = retrieve_answers(our_query)
print(answer)