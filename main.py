import spacy
from transformers import pipeline

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load a transformer-based conversational model
chat_model = pipeline("conversational", model="microsoft/DialoGPT-medium")

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.")
    context = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Process input with spaCy
        doc = nlp(user_input)
        print("Entities detected:", [(ent.text, ent.label_) for ent in doc.ents])

        # Generate a response with the transformer model
        context.append(user_input)
        response = chat_model(" ".join(context))
        print("Bot:", response[0]["generated_text"])

if __name__ == "__main__":
    chatbot()