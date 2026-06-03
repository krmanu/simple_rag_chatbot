import os
from dotenv import load_dotenv

from utlis.retriever import load_retriever
from langchain_groq import ChatGroq
from utlis.guardrail import input_guardrail, output_guardrail

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
retriever = load_retriever()

llm = ChatGroq(model_name="openai/gpt-oss-120b", api_key=groq_api_key)

def rag_chat(query):

    is_valid, error = input_guardrail(query)
    if not is_valid:
        print(f"Error: {error}")
        return

    docs = retriever.invoke(query)
    
    sources = []
    for doc in docs:
        sources.append(doc.metadata["source"])
        
    context ="\n\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)
    final_response = output_guardrail(
        response.content
    )
    return final_response, sources