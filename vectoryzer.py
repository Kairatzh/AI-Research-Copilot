"""
    Модуль для построение RAG систем с использованием векторных баз данных.
"""
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_vector_store(texts, persist_directory="vector_store"):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = []
    for text in texts:
        chunks = text_splitter.split_text(text)
        for chunk in chunks:
            docs.append(Document(page_content=chunk))
    
    embeddings = OpenAIEmbeddings()
    
    vector_store = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    
    return vector_store
