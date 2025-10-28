# langsmith-rag  

End-to-end **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain**, **OpenAI**, and **FAISS** to query **LangSmith documentation**.  

---
### Web Knowledge Retrieval using LangChain and OpenAI (RAG Pipeline)

This project demonstrates how to build an **end-to-end Retrieval-Augmented Generation (RAG) system** that can read, store, and answer questions from real web content.  

- **Data Source:** Scraped content directly from the **LangSmith documentation** using LangChain’s `WebBaseLoader`.  
- **Preprocessing:** Split long documents into smaller, overlapping text chunks with **`RecursiveCharacterTextSplitter`** for better context handling.  
- **Embeddings:** Generated semantic embeddings using **OpenAI’s text-embedding model** to convert text into numerical representations.  
- **Vector Database:** Stored embeddings in a **FAISS vector index** to enable **fast and accurate similarity search**.  
- **Retrieval + Generation:** Used **LangChain retrievers and document chains** with **GPT-4** to produce **context-aware answers** grounded in the retrieved documents.  
- **Outcome:** Demonstrated the **complete workflow of a modern RAG pipeline**, combining retrieval accuracy with natural language generation for intelligent information access.

  ---


## Overview  

This project walks through how to **build a Retrieval-Augmented Generation (RAG) system from scratch**. It takes information from the web, organizes it, and uses that data to answer questions accurately with **GPT-4**.  

The process begins by **scraping content** from the LangSmith documentation using **WebBaseLoader**. The raw text is then **split into small overlapping chunks** with **RecursiveCharacterTextSplitter**, ensuring the model retains context across sections. Each chunk is **converted into embeddings** with **OpenAI’s embedding** model and stored in a **FAISS vector database** for fast similarity search.  

When a user asks a question, the **retriever searches the FAISS index** for the most relevant chunks of text. Those chunks, along with the query, are sent to **GPT-4**, which generates a clear, grounded answer based on the original documentation.  

This setup mirrors how real-world RAG systems power **knowledge assistants, document search tools, and domain-specific chatbots**. It combines **retrieval for accuracy** and **generation for fluency**, creating reliable, context-driven answers.  

**In short, this project covers every part of a modern RAG pipeline:**  
- **Collecting data** from the web  
- **Splitting and preparing text**  
- **Creating embeddings**  
- **Storing vectors** in FAISS  
- **Querying GPT-4** for context-based answers  

---

## Tech Stack  

- **LangChain** – handles document loading, text splitting, retrieval, and prompt management  
- **OpenAI (GPT-4 + embeddings)** – generates embeddings and contextual responses  
- **FAISS** – provides efficient vector similarity search  
- **Python & dotenv** – for environment configuration and setup  

---

## Project Workflow  

1. **Load environment variables** with `dotenv`  
2. **Scrape data** using `WebBaseLoader`  
3. **Split documents** using `RecursiveCharacterTextSplitter`  
4. **Create embeddings** with `OpenAIEmbeddings`  
5. **Store vectors** in **FAISS**  
6. **Build retrieval and document chains** using LangChain  
7. **Query the LLM** for context-aware responses  

---
