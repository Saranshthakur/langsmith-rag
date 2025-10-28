# Langsmith-rag

End-to-end Retrieval-Augmented Generation (RAG) pipeline using **LangChain**, **OpenAI**, and **FAISS** to query LangSmith documentation.

---

##  Overview
This project demonstrates how to build a complete **RAG (Retrieval-Augmented Generation)** pipeline from scratch — starting from web data ingestion to generating context-aware answers using GPT-4.  
It scrapes LangSmith documentation, splits the content into chunks, creates embeddings, stores them in a FAISS vector database, and retrieves the most relevant chunks to answer user queries.

---

##  Tech Stack
- **LangChain** – pipeline orchestration, document loaders, retrievers, and prompt templates  
- **OpenAI (GPT-4o + embeddings)** – for generating vector representations and responses  
- **FAISS** – high-speed vector similarity search  
- **Python & dotenv** – for environment management and configuration  

---

## Project Workflow
1. **Load Environment Variables** using `dotenv`
2. **Scrape Data** using `WebBaseLoader` from LangChain community loaders
3. **Split Documents** into overlapping text chunks using `RecursiveCharacterTextSplitter`
4. **Create Embeddings** via `OpenAIEmbeddings`
5. **Store Vectors** in a FAISS vector database
6. **Build Retrieval & Document Chains** using LangChain abstractions
7. **Query the LLM** for context-aware responses

---

