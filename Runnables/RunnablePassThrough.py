from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="write a good humorous joke about the {topic}",
    input_variables=['topic']
    )
prompt2 = PromptTemplate(
    template="Explain the following joke -{text}",
    input_variables=['text']
    )

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = ({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
result = final_chain.invoke({"topic":"Life"})
print(result)
