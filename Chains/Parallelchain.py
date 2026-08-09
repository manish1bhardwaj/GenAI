from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a simple study notes from the following text \n{text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="Generate the 5 questions with Multiple choice Options from the following text \n{text}",
    input_variables=["text"]
)
prompt3 = PromptTemplate(
    template="merge both the provided notes and quiz into a single document \n notes->{notes} and quiz->{quiz}",
    input_variables=["notes","quiz"]
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes':prompt1|model|parser,
    'quiz':prompt2|model|parser
})

merge_chain = prompt3|model|parser

chain = parallel_chain|merge_chain|parser
text = """Generative artificial intelligence, unlike its predecessors, can create new content by extrapolating from its training data. Its extraordinary ability to produce human-like writing, images, audio, and video have captured the world’s imagination since the first generative AI consumer chatbot was released to the public in the fall of 2022. GenAI now powers a range of consumer and professional applications and services that help save time, money, and effort.

But every action has an equal and opposite reaction. So, along with its remarkable productivity prospects, generative AI brings new potential business risks—such as inaccuracy, privacy violations, and intellectual property exposure—as well as the capacity for large-scale economic and societal disruption. For example, generative AI’s productivity benefits are unlikely to be realized without substantial worker retraining efforts and, even so, will undoubtedly dislocate many from their current jobs. Consequently, government policymakers around the world, and even some technology industry executives, are advocating for rapid adoption of AI regulations.

This article is an in-depth exploration of the promise and peril of generative AI: How it works; its most immediate applications, use cases, and examples; its limitations; its potential business benefits and risks; best practices for using it; and a glimpse into its future.

What Is Generative AI (GenAI)?
Generative AI (GAI) is the name given to a subset of AI machine learning technologies that have recently developed the ability to rapidly create content in response to text prompts, which can range from short and simple to very long and complex. Different generative AI tools can produce new audio, image, and video content, but it is text-oriented conversational AI that has fired imaginations. In effect, people can converse with, and learn from, text-trained generative AI models in pretty much the same way they do with humans.

Generative AI took the world by storm in the months after ChatGPT, a chatbot based on OpenAI’s GPT-3.5 neural network model, was released on November 30, 2022. GPT stands for generative pretrained transformer, words that mainly describe the model’s underlying neural network architecture.

There are many earlier instances of conversational chatbots, starting with the Massachusetts Institute of Technology’s ELIZA in the mid-1960s. But most previous chatbots, including ELIZA, were entirely or largely rule-based, so they lacked contextual understanding. Their responses were limited to a set of predefined rules and templates. In contrast, the generative AI models emerging now have no such predefined rules or templates. Metaphorically speaking, they’re primitive, blank brains (neural networks) that are exposed to the world via training on real-world data. They then independently develop intelligence—a representative model of how that world works—that they use to generate novel content in response to prompts. Even AI experts don’t know precisely how they do this as the algorithms are self-developed and tuned as the system is trained.

Businesses large and small should be excited about generative AI’s potential to bring the benefits of technology automation to knowledge work, which until now has largely resisted automation. Generative AI tools change the calculus of knowledge work automation; their ability to produce human-like writing, images, audio, or video in response to plain-English text prompts means that they can collaborate with human partners to generate content that represents practical work.

“The Oracle Cloud trains dozens of AI models and embeds hundreds of AI agents in cloud applications,” Larry Ellison, chairman and chief technology officer of Oracle, said during the company’s December 2024 earnings call.

“Oracle's AI agents automate drug design, image and genomic analysis for cancer diagnostics, audio updates to electronic health records for patient care, satellite image analysis to predict and improve agricultural output, fraud and money laundering detection, dual factor biometric computer logins, and real-time video weapons detection in schools."""
result = chain.invoke({"text":text})
# print(result)

chain.get_graph().print_ascii()