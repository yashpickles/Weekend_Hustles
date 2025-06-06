from dotenv import load_dotenv
from pydantic import BaseModel
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
import wikipedia
import os
from huggingface_hub import login
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from tools.duckduckgo_searcher import web_search
from tools.math_solver import solve_math_expression, get_math_task


# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN_KEY")
os.environ["HF_HOME"] = os.path.join(os.getcwd(), ".cache")

if hf_token is None:
    raise ValueError("HUGGINGFACE_TOKEN_KEY is not set in .env")

# Authentication
login(token=hf_token)

# S1 Setting Up LLM for it's 
llm = "MBZUAI/LaMini-Flan-T5-783M"
print(f'Loading Model: {llm}')
tokenizer = AutoTokenizer.from_pretrained(llm)
model = AutoModelForSeq2SeqLM.from_pretrained(llm)
qa_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=0)

# S2 AI Agent Skeleton
class QueryInput(BaseModel):
    
    question: str
    max_chars: int = 512 # Max Characters to be extracted from Wikipedia

class AiAgent:

    def __init__(self, pipeline):
        self.pipeline = pipeline

    # Extract Relevant Data from question (patch == v1.2)
    @staticmethod  # (patch == v1.3)
    def clean_topic(question: str) -> str:
        tokens = question.lower().split()
        keywords = [c_word for c_word in tokens if c_word not in ENGLISH_STOP_WORDS]
        return " ".join(keywords)

    # Wiki Context Extractor 
    def wiki_context(self, topic: str, max_chars: int = 512) -> tuple[str, str]:
        try:
            # Search for a matching page title  (patch == v1.3)
            search_results = wikipedia.search(topic)
            if not search_results:
                suggested = wikipedia.suggest(topic)
                if suggested:
                    print(f"No exact match found. Trying suggested topic: {suggested}")
                    topic = suggested
                    search_results = wikipedia.search(suggested)
                else: 
                    return topic, "Sorry, I couldn't find that topic on Wikipedia."
            
            # Use top matching results as that actual page title
            page_title = search_results[0]
            page = wikipedia.page(title=page_title, auto_suggest= False)
            content = page.summary[:max_chars]
            return page_title, content
        
        except wikipedia.exceptions.DisambiguationError as e:
            return topic, f"Confusing Topic: Did you mean: {', '.join(e.options[:5])}"
        except wikipedia.exceptions.PageError as e:
            return topic, f"Sorry, I couldn't find that topic on Wikipedia. "

    # Answer Generator    
    def reseach_response(self, question: str, context:str, topic: str, source_url: str)  -> dict:
        prompt = (
                f"Context:\n{context}\n\n"
                f"Answer the question clearly and factually.\n"
                f"Question: {question}\n"
                f"Answer:"
                )
        # Wikipedia answer generator
        result = self.pipeline(prompt, 
                               max_new_tokens=768, 
                               do_sample=True, 
                               temperature=0.85,
                               top_p = 0.92,
                               top_k = 50, 
                               repetition_penalty = 1.15
                               )
        summary = result[0]['generated_text']

        return{
            "topic": topic,
            "summary": summary,
            "sources": [source_url],
            "tools_used": ["wikipedia", "transformers", "MBZUAI/LaMini-Flan-T5-783M"]
        }
    
    # Run the AI Agent
    def run(self, input_data: QueryInput) -> dict:
        raw_question = input_data.question
        topic = self.clean_topic(raw_question) # (patch == v1.2)


        # Math Problem Solver
        math_keywords = ["integrate", "differentiate", "simplify", "solve", "equation", "derivative", "derivate", "unscramble"]
        if any(m_word in topic for m_word in math_keywords):
            task = get_math_task((input_data.question))
            math_result = solve_math_expression(input_data.question, task=task)
            return{
                "topic": input_data.question,
                "summary": math_result,
                "sources": ["Zee Mathz Tool( Best Arnold Impression!!)"],
                "tools_used": ["sympy"]
            }
        
        # web seach generator
        web_keywords = ["latest", "breaking", "news", "daily", "trending", "top", "who won", "today", "web", "internet"]
        if any (w_word in topic for w_word in web_keywords):
            web_results = web_search(input_data.question, max_results=5)
            summary = "\n".join(web_results)
            return{
                "topic": input_data.question,
                "summary": summary,
                "sources": web_results,
                "tools_used": ["duckduckgo"]
            }

        # wikipedia answer generator
        page_title, context = self.wiki_context(topic, input_data.max_chars)
        print(f"→ Cleaned topic: {topic}")
        print(f"→ Wikipedia Page Selected: {page_title}")

        if context.startswith("Sorry") or context.startswith("Confusing"):
            return{
                "topic": topic,
                "summary": context,
                "sources": [],
                "tool_used": ["wikipedia"]
            }
        wiki_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
        return self.reseach_response(raw_question, context, page_title, wiki_url)


# S3: Usage
if __name__ == "__main__":
    question = input("Ask me Anything: ")
    user_input = QueryInput(question=question)
    agent = AiAgent(qa_pipeline)
    answer = agent.run(user_input)
    print("\n Response:\n", answer)

    
    


