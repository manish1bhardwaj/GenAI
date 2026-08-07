from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint( repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give 3 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)
prompt = template.invoke({'topic':"BlackHole"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)


# This is because you're using LangChain 1.x, while the code you're following is written for older LangChain (0.x).

# Your installed packages are:

# langchain-core            1.5.3
# langchain-huggingface     1.2.2

# But you don't have the langchain package:

# pip show langchain

# WARNING: Package(s) not found: langchain

# That's why Python says:

# ModuleNotFoundError: No module named 'langchain.output_parsers'