from django.shortcuts import render
from .retrieve import get_rag_docs
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
def prompt_rag(prompt: str) -> str:
    model = get_model()
    embedding = model.encode([prompt])[0]
    docs = get_rag_docs(6, embedding)
    docs = [doc[2] for doc in docs] # doc[2] is the content of the document

    # Format context with clear structure (BEST PRACTICE)
    if docs:
        context_sections = []
        for i, doc_content in enumerate(docs, 1):
            context_sections.append(f"[Document {i}]\n{doc_content}\n")
        formatted_context = "\n".join(context_sections)
    else:
        formatted_context = "No relevant documents found."

    print(formatted_context)

    full_prompt = f"""You are an expert counselor specializing in college applications and helping students with their college applications.

## CONTEXT DOCUMENTS
The following documents have been retrieved as potentially relevant to answer the question. Documents are ordered by relevance (most relevant first).

{formatted_context}

## CRITICAL INSTRUCTIONS - READ CAREFULLY

**HOW TO USE CONTEXT AND GENERAL KNOWLEDGE:**

1. **When Context is Relevant**: If the context documents contain information that directly answers the question, use that information as your primary source.

2. **When Context is Missing or Irrelevant**: 
   - If the context documents do NOT contain the information needed, you MUST immediately use your general knowledge to answer the question.
   - DO NOT state that "the documents do not contain information" or "the documents do not offer information about X".
   - DO NOT leave any part of the question unanswered.
   - You MUST provide a complete, comprehensive answer using your general knowledge.
   - Treat this as a REQUIREMENT, not a suggestion.

3. **Combining Sources**: You can seamlessly combine information from context documents with your general knowledge to provide the most complete answer possible.

4. **Other Requirements**:
   - Only use information from context documents that directly relates to the question. Ignore irrelevant information.
   - Do not cite specific documents or mention document numbers. Integrate information naturally.
   - Provide a clear, concise answer without repeating information.
   - Organize your response with appropriate headings and formatting.

## QUESTION
{prompt}

## RESPONSE
Provide a complete, comprehensive answer to the question. If the context documents contain relevant information, use it. If they don't, use your general knowledge to provide a thorough answer. Never indicate that information is missing - always provide a complete response."""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=full_prompt
    )

    return response.text






