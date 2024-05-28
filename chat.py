import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Assuming the Chroma vector database has already been created and persisted
# in the directory specified by DB_DIR
ABS_PATH: str = os.path.dirname(os.path.abspath(__file__))
DB_DIR: str = os.path.join(ABS_PATH, "db")

huggingface_embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

# Load the persisted Chroma vector database
vectordb = Chroma(persist_directory=DB_DIR, embedding_function=huggingface_embeddings)

# Define a function to search the Chroma vector database with a query
def search_chroma_db(query):
    # Search the vector database with the given query
    results = vectordb.similarity_search(query)
    
    # Return the search results
    return results

# Example usage
if __name__ == "__main__":
    query = "What is design study?"
    search_results = search_chroma_db(query)
    print(search_results)
