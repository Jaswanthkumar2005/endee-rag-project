# Endee RAG Project – Document Question Answering System

## Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** based document question answering system.  
The system allows users to ask questions and get relevant answers from documents using **vector search**.

The core idea of this project is to demonstrate how **vector embeddings** can be stored and searched efficiently, with **Endee used as the vector database layer**.

---

## Problem Statement

Searching information from large text documents using traditional keyword search is inefficient and inaccurate.  
This project solves the problem by converting documents into **vector embeddings** and retrieving the most relevant content based on **semantic similarity**.

---

## Use Case

**Document Question Answering (RAG)**

- Input: Text documents
- User asks a natural language question
- System retrieves the most relevant document chunk
- The retrieved content is returned as the answer

---

## System Design / Technical Approach

The system works in the following steps:

1. Documents are loaded from text files  
2. Text is split into smaller chunks  
3. Each chunk is converted into vector embeddings  
4. Embeddings are stored in the vector database (Endee)  
5. User query is converted into an embedding  
6. Vector similarity search is performed  
7. The most relevant content is returned  

**Flow:**
Documents → Embeddings → Endee Vector Store → Similarity Search → Answer


---

## How Endee is Used

Endee is used as the **vector database layer** in this project.

- Document embeddings are stored in a vector store
- Vector similarity search logic follows Endee concepts
- Demonstrates how Endee can be used in RAG-based systems
- Aligns with real-world semantic search applications

---

## Project Structure

endee-rag-project/

│

├── data/

│ └── documents.txt

├── src/

│ ├── ingest.py

│ ├── search.py

│ └── rag.py

├── requirements.txt

├── README.md

└── .gitignore

