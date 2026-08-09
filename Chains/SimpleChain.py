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

template = PromptTemplate(
    template= "Generate 5 interesting quotes about {topic} and mention the name of the writer" ,
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = template|model|parser
result = chain.invoke({"topic":"self-confidence"})
print(result)
chain.get_graph().print_ascii()