import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open("intents.json")as file:
  intents = json.load(file)["intents"]

vectorizer = TfidfVectorizer()
patterns = []
tags = []
patterns = []
tags = []
for intent in intents:
  for pattern in intent["patterns"]:
    patterns.append(pattern)
    tags.append(intent["tag"])
X = vectorizer.fit_transform(patterns)

classifier = LogisticRegression()
classifier.fit(X, tags)


# === Memory ===
memory = {}

# === Process Input ===
def process_input(user_input):
    user_input = user_input.lower()

    # Remember name
    if "my name is" in user_input:
        name = user_input.split("is")[-1].strip().capitalize()
        memory["name"] = name
        return f"Nice to meet you, {name}!"

    # Recall name
    elif "what is my name" in user_input:
        return f"Your name is {memory.get('name', 'not known yet')}."

    else:
        return None  # Let intent classifier handle it

# === Chatbot Main Logic ===
def chatbot_response(inp):
    special_response = process_input(inp)
    if special_response:
        return special_response

    inp_vec = vectorizer.transform([inp])
    predicted_tag = classifier.predict(inp_vec)[0]

    for intent in intents:
        if intent["tag"] == predicted_tag:
            response = random.choice(intent["responses"])
            return response

    return "I'm here to help! Ask me something."

