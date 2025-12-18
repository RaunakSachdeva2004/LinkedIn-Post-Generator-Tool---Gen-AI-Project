from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(model ="openai/gpt-oss-120b" )

if __name__ == "__main__":
    respomse = llm.invoke("What are the two most important ingredietns in samosa")
    print(respomse.content)