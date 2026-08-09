from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description="Give the sentiment of the following feedback")
parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into Positive and Negative \n{feedback} \n {format_instruction} ",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an Appropriate feedback to this Positive feedback \n{feedback} ",
    input_variables=["feedback"],
)
prompt3 = PromptTemplate(
    template="Write an Appropriate feedback to this Negative feedback \n{feedback} ",
    input_variables=["feedback"],
)
parser = StrOutputParser()

classifier_chain = prompt1|model|parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive",prompt2|model|parser),
    (lambda x:x.sentiment == "negative",prompt3|model|parser),
    RunnableLambda(lambda x:"Could not Find any sentiment")
)

chain = classifier_chain|branch_chain

result = chain.invoke({"feedback":"What is this"})
print(result)
chain.get_graph().print_ascii()