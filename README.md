# RAG-Based Knowledge Assistant

A **Retrieval-Augmented Generation (RAG)** project that allows users to ask questions about PDFs and get accurate AI-generated answers.This project combines **document embeddings**, **semantic search**, and **language model generation** to create a smart knowledge assistant.

---

## 🚀 Features

- Upload and process PDF documents  
- Split text into manageable chunks for efficient retrieval  
- Generate vector embeddings for semantic understanding  
- Retrieve relevant content using similarity search  
- Generate answers using AI models based on retrieved content  

---

## 🛠️ Tech Stack

- **Python** – Core programming language  
- **FAISS** – Vector similarity search  
- **OpenAI Embeddings** – Text embeddings  
- **LangChain** – RAG pipeline orchestration  
- **PyPDF2** – PDF text extraction  
- **Gradio / Streamlit (optional)** – Web interface for interactive use  

---

## 📂 Project Structure
rag-knowledge-assistant/
│
├─ Backend/
│ ├─ embedder.py # Create text embeddings
│ ├─ generator.py # Generate answers
│ ├─ pdf_loader.py # Load PDF documents
│ ├─ retriever.py # Search relevant chunks
│ └─ text_chunker.py # Split text into smaller chunks
│
├─ Data/
│ └─ sample.pdf # Example PDF
│
├─ Frontend/ # Optional: web interface
├─ requirements.txt # Project dependencies
└─ README.md


---

## ⚡ How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/bunty03/rag-knowledge-assistant.git
cd rag-knowledge-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3.**Run the main script**
```bash
python Backend/main.py --pdf Data/sample.pdf --query "Your question here"
```
4. **Optional: Launch web interface**
```bash
streamlit run Frontend/app.py
# or
gradio app.py
```
> Ask questions about any PDF and get precise AI-generated answers instantly!  
> Combines semantic search, embeddings, and language models for smart knowledge retrieval.
