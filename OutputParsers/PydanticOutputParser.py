from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint( repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name : str = Field(description="Name of the person")
    age : int = Field(gt=18,description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Generate the name ,age and city of a fictional {place} person \n{format_instruction}",
    input_variables=["place"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt = template.invoke({'place':"indian"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

chain = template|model|parser

result = chain.invoke({'place':"indian"})
print(result)