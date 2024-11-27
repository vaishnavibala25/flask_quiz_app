from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Sample questions
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 2+2?", "options": ["3", "4", "5"], "answer": "4"}
]

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, question in enumerate(questions):
            user_answer = request.form.get(f'question-{i}')
            if user_answer == question['answer']:
                score += 1
        return redirect(url_for('main.result', score=score))
    return render_template('quiz.html', questions=questions)

@main.route('/result')
def result():
    score = request.args.get('score', 0, type=int)
    return render_template('result.html', score=score)
