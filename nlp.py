import json

data = {
    "intents": [
                {
            "tag": "masarweh is my devoloper",
            "patterns": [
                "who made you ?",
                "Do you know ",
                "masarweh?",
                "how do you work?",
                "friends"
            ],
            "responses": [
                "mohammad masarweh is my devoloper he studied and researched all concepts in ai and python to devolop me and cmic_bot my twin XD.",
                "you can ask mohammad masarweh about how i work :) "
            ]
        },

        {
            "tag": "explain_OOP",
            "patterns": [
                "What is OOP?",
                "Explain object-oriented programming",
                "Tell me about classes and objects",
                "how does OOP work?",
                "Can you explain inheritance?"
            ],
            "responses": [
                "OOP stands for Object-Oriented Programming. It organizes code into classes and objects to model real-world concepts.",
                "In Python, OOP lets you define classes to bundle data and behavior. Want an example?",
                "Sure! Here's a simple class:\n\n```python\nclass Animal:\n    def speak(self):\n        print(\"I make sound\")\n```"
            ]
        },
        {
            "tag": "what_is_variable",
            "patterns": [
                "what is a variable?",
                "define variable",
                "explain python variable",
                "how do I use variables?"
            ],
            "responses": [
                "A variable in Python is a name that stores data. Example:\n\n```python\nx = 5\nprint(x)\n```",
                "Think of a variable as a labeled box that holds a value, like a number or string."
            ]
        },
        {
            "tag": "how_does_chatbot_work",
            "patterns": [
                "how does a chatbot work?",
                "explain chatbot architecture",
                "how do you build a chatbot?",
                "what makes a chatbot smart?"
            ],
            "responses": [
                "A chatbot uses NLP to understand text, then maps it to an intent, and responds based on logic or a model.",
                "Chatbots work by detecting patterns in text and matching them with predefined intents or AI-generated replies.",
                "They can be rule-based or AI-powered. Want to build one from scratch?"
            ]
        },
        {
            "tag": "nlp_from_scratch",
            "patterns": [
                "how to learn NLP?",
                "start NLP from zero",
                "teach me NLP",
                "I want to build an NLP model"
            ],
            "responses": [
                "To start NLP: learn text preprocessing, tokenization, vectorization, and basic classification models.",
                "A good path is: 1) Clean text, 2) Use Bag of Words/TF-IDF, 3) Train a classifier. Ready to try?",
                "Let’s begin with tokenizing a sentence. Example:\n\n```python\nfrom nltk.tokenize import word_tokenize\nword_tokenize(\"Hello NLP world!\")\n```"
            ]
        },
        {
            "tag": "ask_python_code",
            "patterns": [
                "give me a code with python",
                "code?",
                "can you show me a Python code example?",
                "python code"
            ],
            "responses": [
                "Sure! Here's an example of Python code: \n\n```python\ndef greet(name):\n    return f\"Hello, {name}!\"\n\nprint(greet(\"world\"))\n```",
                "Let me show you a Python snippet:\n\n```python\nfor i in range(5):\n    print(i)\n```"
            ]
        },
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hello", "Hey", "Good morning", "Good evening"],
            "responses": ["Hello! I'm MS_him_and, your teacher. How can I help you today?", "Hi there! Ready to learn something new?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "Goodbye", "See you later"],
            "responses": ["Goodbye! Keep learning and feel free to come back any time.", "See you later!"]
        },
        {
            "tag": "ask_python_definition",
            "patterns": ["What is Python?", "Define Python", "Explain Python"],
            "responses": [
                "Python is an interpreted, high-level, general-purpose programming language.",
                "Python is a powerful language known for its simplicity and versatility."
            ]
        },
        {
            "tag": "ask_what_is_nlp",
            "patterns": ["What is NLP?", "Define NLP", "Explain Natural Language Processing"],
            "responses": [
                "NLP stands for Natural Language Processing—it's a field of AI that focuses on the interaction between computers and human language.",
                "NLP is about teaching machines to understand and generate human language."
            ]
        },
        {
            "tag": "ask_for_help",
            "patterns": ["Can you help me?", "I need help", "Help please"],
            "responses": [
                "Of course! Let me know what topic you'd like to dive into.",
                "Sure, I'm here to help. What do you need assistance with?"
            ]
        },
        {
            "tag": "teach_concept",
            "patterns": ["Teach me about classes in Python", "What is a class in Python?", "How do I use classes?"],
            "responses": [
                "A class in Python is a blueprint for creating objects that encapsulates data and functions.",
                "In Python, classes allow you to create objects with their own attributes and methods."
            ]
        },
        {
            "tag": "intro_data_science",
            "patterns": [
                "What is data science?",
                "Explain data science",
                "Define data science",
                "Tell me about data science"
            ],
            "responses": [
                "Data science is the field of extracting insights from data using statistics, programming, and machine learning.",
                "It involves cleaning, analyzing, and modeling data to solve real-world problems."
            ]
        },
        {
            "tag": "python_for_data_science",
            "patterns": [
                "How is Python used in data science?",
                "Why is Python good for data science?",
                "Python and data science",
                "Python libraries for data science"
            ],
            "responses": [
                "Python is popular in data science due to libraries like pandas, NumPy, scikit-learn, and matplotlib.",
                "Python's syntax is easy, and it has powerful tools for data manipulation and machine learning."
            ]
        },
        {
            "tag": "pandas_intro",
            "patterns": [
                "What is pandas?",
                "Explain pandas in Python",
                "How to use pandas",
                "pandas examples"
            ],
            "responses": [
                "Pandas is a Python library for working with structured data, especially DataFrames.",
                "It lets you load, manipulate, and analyze tabular data easily.",
                "Here's a pandas example:\n\n```python\nimport pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())\n```"
            ]
        },
        {
            "tag": "data_cleaning",
            "patterns": [
                "How to clean data in Python?",
                "Data preprocessing steps",
                "Handle missing values",
                "How do I clean a dataset?"
            ],
            "responses": [
                "You can clean data using pandas: drop nulls, fill missing values, remove duplicates.",
                "Example:\n\n```python\ndf.dropna(inplace=True)\ndf.fillna(0, inplace=True)\ndf.drop_duplicates(inplace=True)\n```"
            ]
        },
        {
            "tag": "data_visualization",
            "patterns": [
                "How to visualize data in Python?",
                "Data visualization libraries",
                "matplotlib example",
                "Plot graphs in Python"
            ],
            "responses": [
                "Use matplotlib, seaborn, or plotly to visualize data.",
                "Here's a simple matplotlib plot:\n\n```python\nimport matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [4, 5, 6])\nplt.show()\n```"
            ]
        },
        {
            "tag": "machine_learning",
            "patterns": [
                "What is machine learning?",
                "Explain ML",
                "How does machine learning work?",
                "ML in data science"
            ],
            "responses": [
                "Machine learning is a method where computers learn patterns from data to make decisions.",
                "It's a core part of data science, used for predictions, classifications, and more."
            ]
        }
    ]
}

with open("intents.json", "w") as file:
    json.dump(data, file, indent=2)

print("intents.json file has been created!")