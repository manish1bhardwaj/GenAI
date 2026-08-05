from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",
                          task = "text-generation")
model = ChatHuggingFace(llm = llm)

messages = [
    SystemMessage(content="You are a Helpful Assistant"),
    HumanMessage(content = "Tell me About Langchain and its components")
    ]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)