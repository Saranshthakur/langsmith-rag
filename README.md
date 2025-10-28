langsmith-rag

End-to-end Retrieval-Augmented Generation (RAG) pipeline using LangChain, OpenAI, and FAISS to query LangSmith documentation.

Overview

This project walks through how to build a Retrieval-Augmented Generation (RAG) system from scratch. It takes information from the web, organizes it, and uses that information to answer questions accurately with GPT-4.

The process begins by scraping content from the LangSmith documentation using WebBaseLoader. The raw text is then split into small overlapping chunks with RecursiveCharacterTextSplitter, so context is preserved across sections. Each chunk is converted into numerical embeddings with OpenAI’s embedding model, then stored in a FAISS database for fast vector search.

When a user asks a question, the retriever searches the FAISS index to find the most relevant text chunks. Those chunks are passed along with the query to GPT-4, which generates a clear, grounded answer based on the original documentation.

This approach mirrors how RAG systems are used in real-world applications like internal knowledge assistants, document search tools, and domain-specific chatbots. It combines retrieval for factual grounding with generation for fluent, human-like responses.

In short, the project covers every part of a modern RAG pipeline:

Collecting data from the web

Splitting and preparing text

Creating embeddings

Storing vectors in FAISS

Using GPT-4 for context-aware answers

Tech Stack

LangChain – handles document loading, text splitting, retrieval, and prompt management

OpenAI (GPT-4 + embeddings) – generates embeddings and contextual responses

FAISS – provides efficient vector similarity search

Python & dotenv – used for environment configuration and setup

Project Workflow

Load environment variables with dotenv

Scrape data using WebBaseLoader

Split documents with RecursiveCharacterTextSplitter

Create embeddings with OpenAIEmbeddings

Store vectors in FAISS

Build retrieval and document chains using LangChain

Query the LLM for context-aware answers
