import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

if __name__ == '__main__':

    os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
    documents = SimpleDirectoryReader("data").load_data()

    #check if 'index' folder exist
    if not os.path.exists("index") and not os.path.isdir("index"):
        os.mkdir("index")
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir="index")

    storage_context = StorageContext.from_defaults(persist_dir="index")

    # uncomment if you want index your document in 'data' folder
    #index = VectorStoreIndex.from_documents(documents)
    #index.storage_context.persist(persist_dir="index")

    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()

    st.title("My favorite chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = query_engine.query(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})



