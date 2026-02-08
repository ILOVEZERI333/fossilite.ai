from django.shortcuts import render
from .retrieve import get_cds_rag_docs, get_college_application_rag_docs
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from google import genai
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_MODEL = os.getenv('GEMINI_MODEL')
client = genai.Client(api_key=GEMINI_API_KEY)

model = None

# Create your views here.


#TESTING PURPOSES ONLY - COMMENT OUT WHEN NOT TESTING
# additional_questions = """
# In addition to the questions above, please answer the following questions:
#     "What are the requirements for a home-based business license?",
#     "How often do I need to file business taxes?",
#     "What insurance is required for a small business?",
#     "What's the difference between a sole proprietorship and an LLC for tax purposes?",
#     "How do I handle employee payroll taxes for my first employee?",
#     "What records should I keep for tax purposes and for how long?",
#     "How do I register my business name if it's different from my personal name?",
#     "What are the common mistakes small businesses make when filing quarterly taxes?",
#     "What are the specific deadlines for filing different types of business taxes throughout the year?",
#     "How do I properly categorize business expenses for tax deductions?",
#     "What compliance requirements do I need to meet if I sell products online across multiple states?",
#     "How should I structure my business if I want to hire contractors vs. employees?",
#     "What are the ongoing administrative tasks I need to complete annually to maintain my business registration?",
#     "I'm starting a side business while working full-time. What administrative steps do I need to take?",
#     "How do I close or dissolve a small business properly?",
#     "What happens if I miss a tax filing deadline for my business?",
#     "Do I need a separate business bank account, and what are the requirements?",
#     "How do I handle business expenses if I work from home?"

# """


def get_model():
    global model
    if model is None:
        model = SentenceTransformer('Qwen/Qwen3-Embedding-0.6B')
    return model

@csrf_exempt
def check_if_essay_required(prompt: str) -> str:


    full_prompt = f"""You are to check if an essay is required for the given pdf of an application. If it is, return True. If it is not, return False. IMPORTANT: If 
    an application requires an essay, it will be stated in the application. If it does not, it will not be stated in the application. DO NOT make up information.
    In addition if the pdf does not contain an essay, look at the context documents to see if the application requires an essay. MAKE SURE THAT THE FIRST WORD OF THE RESPONSE IS TRUE OR FALSE."""

    embedding = model.encode([full_prompt])[0]
    docs = get_cds_rag_docs(6, embedding)

    context = "\n".join([doc[2] for doc in docs])

    full_prompt += f"\n\n## CONTEXT DOCUMENTS\n{context}"

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=full_prompt
    )
    return response.text.split(" ")[0].lower() == "true"

@csrf_exempt
def prompt_cds_rag_application(prompt: str, instruction_prompt: str) -> str:
    """
    General-purpose function for queries that need CDS documents.
    
    Args:
        prompt: The actual content/query text (e.g., application text, question, etc.)
        instruction_prompt: The prompt template/instructions that will be formatted with context and prompt.
                           Should include {formatted_context} and {prompt} placeholders.
    
    Returns:
        The response text from the model.
    """
    model = get_model()
    embedding = model.encode([prompt])[0]
    docs = get_cds_rag_docs(6, embedding)
    docs = [doc[2] for doc in docs] # doc[2] is the content of the document

    # Format context with clear structure (BEST PRACTICE)
    if docs:
        context_sections = []
        for i, doc_content in enumerate(docs, 1):
            context_sections.append(f"[Document {i}]\n{doc_content}\n")
        formatted_context = "\n".join(context_sections)
    else:
        formatted_context = "No relevant documents found."

    # Format the instruction prompt with context and prompt content
    full_prompt = instruction_prompt.format(
        formatted_context=formatted_context,
        prompt=prompt
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=full_prompt
    )

    return response.text

@csrf_exempt
def prompt_college_application_rag_application(prompt: str, instruction_prompt: str) -> str:
    """
    General-purpose function for queries that need college application documents.
    
    Args:
        prompt: The actual content/query text (e.g., application text, question, etc.)
        instruction_prompt: The prompt template/instructions that will be formatted with context and prompt.
                           Should include {formatted_context} and {prompt} placeholders.
    
    Returns:
        The response text from the model.
    """
    model = get_model()
    embedding = model.encode([prompt])[0]
    docs = get_college_application_rag_docs(6, embedding)
    docs = [doc[2] for doc in docs] # doc[2] is the content of the document

    # Format context with clear structure (BEST PRACTICE)
    if docs:
        context_sections = []
        for i, doc_content in enumerate(docs, 1):
            context_sections.append(f"[Document {i}]\n{doc_content}\n")
        formatted_context = "\n".join(context_sections)
    else:
        formatted_context = "No relevant documents found."

    # Format the instruction prompt with context and prompt content
    full_prompt = instruction_prompt.format(
        formatted_context=formatted_context,
        prompt=prompt
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=full_prompt
    )

    return response.text






