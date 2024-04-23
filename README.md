# Chatbot_RAG
Utilize the llama index framework to create a RAG-based chatbot assistant.  Informations are retrivied from PDF documents using a retrieval-augmented pipeline. 
<br><br>
Key Features: 
* Implementation of RAG using the llama index for information retrieval.
* Option to develop a simple front-end using Streamlit
* Along with the response provided the assistant has to provide the references in the document.

## RAG Pipeline ##
The document in pdf format in the 'data' folder contains information about a lawyer. It is an example of a knowledge base that you can query and retrieve some information from.

1. After you set yout OpenAI API key, main.py reads your documents in 'data folder':
  ```
  documents = SimpleDirectoryReader("data").load_data()
  ```
2. Creation of index from document.<br> An Index is a data structure that allows us to quickly retrieve relevant context for a user query. It's the core foundation for retrieval-augmented generation (RAG) use-cases.
  ```
  index = VectorStoreIndex.from_documents(documents)
  ```
3. Query engine is a generic interface that allows you to ask question over your data.
  A query engine takes in a natural language query, and returns a rich response.
  ```
  query_engine = index.as_query_engine()
  ```
4. After setting these components you can query to your document with this:
  ```
  answer = query_engine.query(question)
  ```
## Frontend ##

For fronted there is Streamlit, an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. I choose it for its simplicity and ease of use.


## Run main.py ##

Run main.py with :
```
streamlit run YOUR_PATH_OF_main.py 
```
