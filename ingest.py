from langchian_community.document_loaders import PyPDFLoader
from langchian_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchian_community.vectorstores import FAISS

data = PyPDFLoader("")