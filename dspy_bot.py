import os
from dotenv import load_dotenv
import dspy

# Load environment variables
load_dotenv()

# Configure the Gemini model
llm = dspy.LM(
    model="gemini/gemini-1.5-flash-latest",
    api_key=os.getenv("GEMINI_API_KEY")
)
dspy.configure(lm=llm)

# Define a simple chat signature
class SimpleChat(dspy.Signature):
    """Basic chatbot that responds clearly."""
    question = dspy.InputField()
    answer = dspy.OutputField()

# Create a callable DSPy module
chat_module = dspy.Predict(SimpleChat)

# Inference function
def get_bot_response(message: str) -> str:
    result = chat_module(question=message)
    return result.answer
