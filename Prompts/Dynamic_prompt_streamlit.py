import streamlit as st 
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id = "Qwen/Qwen2.5-7B-Instruct",
                    task = 'text-generation')
model  = ChatHuggingFace(llm=llm)

st.header("Summarizer Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#Template
template = PromptTemplate(
template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present.
- Explain mathematical concepts using simple examples.

2. Analogies:
- Use relatable analogies.

If information is unavailable, reply:
"Insufficient information available."

Ensure the summary is clear and accurate.
""",
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ]
)

#Fill the PlaceHolders
prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
    })

if st.button("Summarize"):
    result = model.invoke(prompt.text)
    st.write(result.content)