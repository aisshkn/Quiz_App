import sqlite3

# Connect to the database (creates quiz.db if it doesn't exist)
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Create the questions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option TEXT NOT NULL
)
''')

# Pre-populate the table with questions
questions = [
    {
        "question": "What is the capital of France?",
        "option_a": "Paris",
        "option_b": "Berlin",
        "option_c": "Madrid",
        "option_d": "Rome",
        "correct_option": "A"
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "option_a": "Python",
        "option_b": "JavaScript",
        "option_c": "C++",
        "option_d": "Java",
        "correct_option": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "option_a": "Venus",
        "option_b": "Mars",
        "option_c": "Jupiter",
        "option_d": "Saturn",
        "correct_option": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "option_a": "Atlantic Ocean",
        "option_b": "Indian Ocean",
        "option_c": "Arctic Ocean",
        "option_d": "Pacific Ocean",
        "correct_option": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "option_a": "William Shakespeare",
        "option_b": "Charles Dickens",
        "option_c": "Jane Austen",
        "option_d": "Mark Twain",
        "correct_option": "A"
    },
    {
        "question": "What is the process by which plants make their food?",
        "option_a": "Respiration",
        "option_b": "Photosynthesis",
        "option_c": "Transpiration",
        "option_d": "Germination",
        "correct_option": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "option_a": "Gold",
        "option_b": "Oxygen",
        "option_c": "Silver",
        "option_d": "Hydrogen",
        "correct_option": "B"
    },
    {
        "question": "What is the square root of 64?",
        "option_a": "6",
        "option_b": "7",
        "option_c": "8",
        "option_d": "9",
        "correct_option": "C"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "option_a": "China",
        "option_b": "Brazil",
        "option_c": "UK",
        "option_d": "Russia",
        "correct_option": "B"
    },
    {
        "question": "What gas do humans need to breathe in order to survive?",
        "option_a": "Carbon Dioxide",
        "option_b": "Nitrogen",
        "option_c": "Oxygen",
        "option_d": "Hydrogen",
        "correct_option": "C"
    },
]

# Insert questions into the database
for q in questions:
    cursor.execute('''
    INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (q["question"], q["option_a"], q["option_b"], q["option_c"], q["option_d"], q["correct_option"]))

# Save and close
conn.commit()
conn.close()

print("Database initialized and questions added!")
