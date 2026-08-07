# 🚀 GenAI & LangChain Learning Repository

Welcome to my **Generative AI & LangChain** repository! This is a hands-on workspace where I continuously learn, experiment, and push code exploring the Generative AI ecosystem using **LangChain**, **Python**, **Streamlit**, and various LLM providers.

---

## 📌 Repository Overview

This repository documents my journey in mastering Generative AI concepts—ranging from basic model invocations and prompt engineering to complex structured outputs, memory management, RAG, and agentic workflows.

---

## 📂 Repository Structure

```text
GenAI-LangChain/
│
├── 📁 Models/               # LLM integrations, Embeddings & Vector similarity notebooks
│   ├── PaidModels_LangChain.ipynb
│   ├── OpenSourceModels.ipynb
│   ├── EmbeddingModels.ipynb
│   └── DocumentSimilarity_App.ipynb
│
├── 📁 Prompts/              # Prompt templates, Chat Templates, History & Streamlit Chat Apps
│   ├── PromptTemplate.py
│   ├── ChatPromptTemplate.py
│   ├── MessagePlaceholder.py
│   ├── ChatHistory_Chatbot.py
│   ├── Basic_Chatbot.py
│   ├── Static_prompt_Streamlit.py
│   └── Dynamic_prompt_streamlit.py
│
├── 📁 OutputParsers/        # Parsing LLM outputs into structured formats
│   ├── StrOutputParser.py
│   ├── JsonOutputParser.py
│   └── StructuredOutputParser.py
│
├── 📁 StructuredOutput/     # Schema enforcing using Pydantic, TypedDict & JSON Schema
│   ├── typeddict_demo.py
│   ├── pydantic_demo.py
│   ├── with_structured_output_typedict.py
│   ├── with_structured_output_pydantic.py
│   └── with_structured_output_json.py
│
├── .env                    # Environment variables (API Keys)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🗺️ Learning Roadmap & Topics Covered

### ✅ Currently Covered
- **Model Integrations:** Connecting with Paid LLMs (OpenAI, Anthropic) and Open-Source models (HuggingFace).
- **Text Embeddings & Vector Math:** Generating embeddings and calculating cosine/document similarity.
- **Prompt Engineering:** Utilizing `PromptTemplate`, `ChatPromptTemplate`, and `MessagesPlaceholder` for dynamic inputs.
- **Chatbots & State:** Managing conversation history and rendering interactive Streamlit chatbot interfaces.
- **Output Parsing:** Enforcing clean text and JSON responses using `StrOutputParser` and `JsonOutputParser`.
- **Structured Outputs:** Forcing deterministic schema outputs using `.with_structured_output()` with `Pydantic` models, `TypedDict`, and `JSON Schema`.

### 🔄 In Progress & Upcoming Topics
- ⚡ **LCEL (LangChain Expression Language):** Declarative chain composition using pipe `|` operators.
- 📚 **Vector Databases & RAG:** Integrating FAISS, Chroma DB, and building Retrieval-Augmented Generation pipelines.
- 🧠 **Advanced Memory:** Buffer memory, Summary memory, and persistent chat sessions.
- 🛠️ **Agents & Tools:** Building autonomous agents with custom tools and function calling.
- 🕸️ **LangGraph:** Creating stateful, multi-agent conversational workflows and loops.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/manish1bhardwaj/GenAI.git
cd GenAI
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API Keys
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## 💻 Running the Examples

- **Run Python Scripts:**
  ```bash
  python Prompts/ChatPromptTemplate.py
  ```

- **Launch Streamlit Chat Apps:**
  ```bash
  streamlit run Prompts/Dynamic_prompt_streamlit.py
  ```

- **Open Jupyter Notebooks:**
  ```bash
  jupyter notebook
  ```

---

⭐ *Feel free to check out the code, star the repo, or follow along as I continuously push new learning modules!*
