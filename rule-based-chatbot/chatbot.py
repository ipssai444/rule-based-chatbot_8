from flask import Flask, render_template, request
import string
from datetime import datetime

app = Flask(__name__)

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

def chatbot_response(user_input):
    clean_input = preprocess(user_input)
    if clean_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"
    elif "how are you" in clean_input:
        return "I'm just a bunch of code, but I'm doing great!"
    elif "name" in clean_input:
        return "My name is ChatBot!"
    elif "help" in clean_input:
        return "I can answer simple questions. Try asking about my name, the date, or say hi!"
    elif "date" in clean_input or "day" in clean_input:
        return f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}."
    elif "time" in clean_input:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "joke" in clean_input:
        return "Why did the Python live on land? Because it was above C level!"
    elif clean_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a lovely day!"
    elif clean_input == "quit":
        return "Exiting the conversation. Bye!"
    else:
        return "Sorry, I don't understand that. Can you rephrase?"

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        response = chatbot_response(user_input)
    return render_template('chat.html', response=response, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
