from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

chain = template1|model|parser|template2|model|parser

result = chain.invoke({'topic':"BlackHole"})
print(result)