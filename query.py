# query.py
from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM 

# Override the global embedding model to use a local model
Settings.embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L12-v2")

# Load your persisted index
storage_context = StorageContext.from_defaults(persist_dir='.index')
index = load_index_from_storage(storage_context)

# Initialize the HuggingFace LLM using a valid checkpoint
llm = HuggingFaceLLM(
    model_name="HuggingFaceTB/SmolLM2-135M-Instruct",
    tokenizer_name="HuggingFaceTB/SmolLM2-135M-Instruct",  # Make sure this matches the model
    # Add other parameters if necessary, e.g., device, max_new_tokens, etc.
)

# Initialize a local embedding model
embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L12-v2")

# Create a query engine that uses the custom LLM and embedding model
query_engine = index.as_query_engine(llm=llm, embed_model=embed_model)

# Querying function
def ask(question):
    response = query_engine.query(question)
    return response

if __name__ == '__main__':
    question = "What are the files in my index?"
    print(ask(question))