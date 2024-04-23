import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

if __name__ == '__main__':

    os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    st.title("My favorite chatbot")

    question = st.text_input("Hello i'm a chatbot, do me a question:")

    while True:
        if question:
            answer = query_engine.query(question)
            for node in answer.source_nodes:
                st.write(f"{node.text}" + f"[page number: {node.metadata['page_label']}]\n")
        question = None
