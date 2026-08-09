from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "generate a short paragraph on this {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Summazire the following /n{text} in 5 points with neat and clean structure",
    input_variables=['text']
)


parser = StrOutputParser()

chain = template1|model|template2|model|parser
result = chain.invoke({"topic":"Covid19"})

print(result)