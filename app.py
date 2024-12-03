from flask import Flask, render_template, request, redirect, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn

# Dashboard route
@app.route('/')
def dashboard():
    performance = session.get('performance', {'attempted': 0, 'correct': 0})
    score = (performance['correct'] / performance['attempted'] * 100) if performance['attempted'] else 0
    performance['score'] = round(score, 2)
    return render_template('dashboard.html', performance=performance)

# Quiz route
@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # Handle answer submission
        user_answer = request.form.get("answer")
        correct_option = request.form.get("correct_option")
        feedback = "Correct!" if user_answer == correct_option else "Incorrect."

        # Update performance in session
        performance = session.get('performance', {'attempted': 0, 'correct': 0})
        performance['attempted'] += 1
        if user_answer == correct_option:
            performance['correct'] += 1
        session['performance'] = performance

        return render_template("feedback.html", feedback=feedback)

    # Fetch a random question from the database
    conn = get_db_connection()
    question_data = conn.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close()

    if question_data is None:
        return "No questions available."

    # Prepare options dictionary
    options = {
        "A": question_data["option_a"],
        "B": question_data["option_b"],
        "C": question_data["option_c"],
        "D": question_data["option_d"]
    }

    return render_template("quiz.html", question=question_data["question"], options=options, correct_option=question_data["correct_option"])

# End quiz route
@app.route('/reset')
def reset_quiz():
    # Clear session data
    session.clear()
    return redirect('/')

@app.route('/end')
def end_quiz():
    # Redirect to the dashboard or home page
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
