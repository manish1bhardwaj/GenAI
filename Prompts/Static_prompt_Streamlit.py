
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id = "Qwen/Qwen2.5-7B-Instruct",
                    task = 'text-generation')

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")
user_input = st.text_input('Enter your prompt')
if st.button('Summarize'):
  result = model.invoke(user_input)
  st.write(result.content)