from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm1=HuggingFaceEndpoint( 
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

llm2 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template="Write a tweet on a {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="generate a Linkedin Post about-{topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1,model1,parser),
    "linkedin":RunnableSequence(prompt2,model2,parser)
})
result = parallel_chain.invoke({"topic":"Kabbadi"})

print(result["tweet"])

print(result["linkedin"])

