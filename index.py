# index.py
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def index(folder):
    # Load documents from the folder
    documents = SimpleDirectoryReader(folder).load_data()
    
    # Initialize the Sentence Transformer embedding model
    embedding_model = HuggingFaceEmbedding(model_name="all-MiniLM-L12-v2")
    
    # Create the index using the sentence transformer embeddings
    index = VectorStoreIndex.from_documents(documents, embed_model=embedding_model)
    
    # Save the index to disk
    index.storage_context.persist(persist_dir='.index')

if __name__ == '__main__':
    index("filter-project/")