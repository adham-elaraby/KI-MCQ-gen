import fitz  # PyMuPDF
import json
import os
import pandas as pd
import traceback
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-4o-mini", temperature=0.5)

TEMPLATE = """
Text:{text}
You are an expert Exam MCQ maker at a University. Given the above text, it is your job to create a quiz of {number} multiple choice questions in {language} for {subject} Students at the Technical University of Darmstadt for their final exam. in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. 
Only pick relevant topics, that would deeply examine their understanding of the course, both in a theoretical and applied sense, and not random questions.
Ensure to make {number} MCQs

Here are a couple of example questions from past exams so that you can get a sense of the difficulty and level: {past_questions}
### RESPONSE_JSON
{response_json}
"""

RESPONSE_JSON = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
    "2": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    }
}

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "language", "past_questions", "response_json"],
    template=TEMPLATE
)

TEMPLATE2 = """
You are an expert {language} grammarian and writer in the field of {subject}. Given a Multiple Choice Quiz for {subject} students. 
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
If the quiz is not at par with the cognitive and analytical abilities of the students, 
update the quiz questions which need to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}

Check from an expert {language} Writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"], 
    template=TEMPLATE2
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain], 
    input_variables=["text", "number", "subject", "tone", "language", "past_questions", "response_json"],
    output_variables=["quiz", "review"], 
    verbose=True,
)

def generate_and_evaluate_mcqs(uploaded_file, number, subject, tone, language, past_questions):
    try:
        pdf_text = ""
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in doc:
            pdf_text += page.get_text()

        with get_openai_callback() as cb:
            response = generate_evaluate_chain({
                "text": pdf_text,
                "number": number,
                "subject": subject,
                "tone": tone,
                "language": language,
                "past_questions": past_questions,
                "response_json": json.dumps(RESPONSE_JSON)
            })

        quiz = response.get("quiz")
        
        # Debugging log to check the content of quiz
        #print("Fragen inhalt vorher (JSON):", quiz)
        
        # Remove unwanted text (e.g., '### RESPONSE_JSON')
        start_index = quiz.find("{")
        if start_index != -1:
            quiz = quiz[start_index:-3]
        
        # Debugging log to check the content of quiz after cleaning
        print("Questions after cleaning and processing (JSON):", quiz)

        if not quiz:
            raise ValueError("Keine Fragen im Quiz! (leer)")

        quiz = json.loads(quiz)
        
        quiz_table_data = []
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join([f"{option}: {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Richtige Lösung": correct})

        return quiz_table_data

    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        print(traceback.format_exc())
        return []
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        return []
