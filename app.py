from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of questions for the quiz
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is the largest planet in the solar system?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"}
]

@app.route('/')
def home():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for idx, question in enumerate(questions):
        user_answer = request.form.get(f'question_{idx}')
        if user_answer == question["answer"]:
            score += 1
    return f'Your score is: {score}/{len(questions)}'

if __name__ == '__main__':
    app.run(debug=True)