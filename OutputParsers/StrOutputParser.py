from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint( repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",)

model = ChatHuggingFace(llm=llm)

#1st Prompt -> detailed report

template1 = PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=["topic"]
)

#2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic':"BlackHole"})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
# chain = template1|model|template2|model
# result = chain.invoke({'topic':"BlackHole"})
# print(result)