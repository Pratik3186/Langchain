# 🚀 LangChain Practice Repository

This repository contains hands-on implementations of **LLMs, Chat Models, and Embeddings** using LangChain and multiple AI providers like OpenAI, HuggingFace, Anthropic, and Google Gemini.

---

## 📌 Project Overview

This project is designed to:

* Learn and experiment with **LangChain 0.3+**
* Understand different **LLM providers**
* Work with **chat models and embeddings**
* Build a strong foundation for **RAG (Retrieval-Augmented Generation)** systems

---

## 📂 Project Structure of LC

```
Langchain/
│── ChatModels/
│   ├── 1_chatmodel_openai.py
│   ├── 2_chatmodel_anthropic.py
│   ├── 3_chatmodels_google.py
│   ├── 4_chatmodel_hf_api.py
│   ├── 5_chatmodel_hf_local.py
│
│── EmbeddedModels/
│   ├── document_similarity.py
│   ├── embedding_hf_local.py
│   ├── embedding_openai_docs.py
│   ├── embedding_openai_query.py
│
│── LLMs/
│
│── venv/              # (ignored)
│── .env              # (not pushed)
│── .gitignore
│── requirements.txt
│── README.md
│── test.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Pratik3186/Langchain.git
cd Langchain
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
GOOGLE_API_KEY=your_google_key
ANTHROPIC_API_KEY=your_anthropic_key
```

---

## 🧠 Features Implemented

### 🔹 Chat Models

* OpenAI Chat Model
* Anthropic Claude
* Google Gemini
* HuggingFace API Models
* HuggingFace Local Models

---

### 🔹 Embeddings

* OpenAI embeddings (query + documents)
* HuggingFace local embeddings
* Document similarity search

---

### 🔹 LLM Basics

* Basic LLM invocation
* Prompt-response workflow

---

## ▶️ Usage

Run any script:

```bash
python ChatModels/1_chatmodel_openai.py
```

Example:

```bash
python EmbeddedModels/document_similarity.py
```

---

## ⚠️ Important Notes

* ❌ Do NOT push:

  * `venv/`
  * `.env`
  * large model files

* ✅ Always use `.gitignore`

* ⚠️ Some APIs require billing (OpenAI)

---

## 🎯 Learning Outcomes

By completing this project, you will understand:

* How LangChain works internally
* Difference between LLMs and Chat Models
* How embeddings power semantic search
* Foundations of RAG systems

---

## 🚀 Next Steps

Planned improvements:

* Build a **Multi-PDF Chat AI (RAG system)**
* Integrate **FAISS / Vector DB**
* Add **Streamlit UI**
* Deploy project

---

## 👨‍💻 Author

**Pratik**
BTech CSE | Aspiring Developer & Researcher

---

## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!

---

