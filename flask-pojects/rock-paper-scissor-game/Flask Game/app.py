from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    message = ""
    global secret_number
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
        except ValueError:
            message = "Please enter a valid integer."
            return render_template('index.html', message=message)
        
        if guess < secret_number:
            message = "Try a higher number."
        elif guess > secret_number:
            message = "Try a lower number."
        else:
            message = f"Congratulations! You guessed the number ({secret_number})."
            secret_number = random.randint(1, 100)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
