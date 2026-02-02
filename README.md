# Endee RAG Project

## Project Overview
This project builds a simple Retrieval Augmented Generation (RAG) system that answers user questions from documents using vector search.

## Problem Statement
Searching information from large text files is difficult. This project solves the problem by using vector embeddings and semantic search.

## System Design
Documents are converted into embeddings and stored in Endee vector database. User queries are also converted into embeddings and matched using vector similarity.

## Endee Usage
Endee is used as the vector database to store and retrieve document embeddings efficiently.

## Setup Instructions
1. Install Python 3.9+
2. Create virtual environment
3. Install dependencies
4. Run ingest.py
5. Run rag.py

## Technologies Used
Python, Sentence Transformers, Endee Vector Database
