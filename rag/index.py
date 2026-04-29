from pathlib import Path
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


pdf_path = Path(__file__).parent / "Spring.pdf"


# Load the PDF file and create a vector store
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

# Split the documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts_chunks = text_splitter.split_documents(documents)

# Create a vector embedding from the text chunks
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = QdrantVectorStore.from_documents(
    documents=texts_chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="spring-pdf",
)
print("Vector store created successfully, and documents indexing completed.")