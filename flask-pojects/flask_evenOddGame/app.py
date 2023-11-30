from flask import Flask, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to a random secret key

# Initialize win and loss counts inside a request context
@app.before_request
def before_request():
    if 'user_wins' not in session:
        session['user_wins'] = 0

    if 'computer_wins' not in session:
        session['computer_wins'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<choice>')
def play(choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result = determine_winner(choice, computer_choice)

    # Update win/loss counts
    if result == "You win!":
        session['user_wins'] += 1
    elif result == "You lose!":
        session['computer_wins'] += 1

    return render_template('result.html', choice=choice, computer_choice=computer_choice, result=result,
                           user_wins=session['user_wins'], computer_wins=session['computer_wins'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

@app.route('/reset')
def reset():
    # Reset win/loss counts
    session['user_wins'] = 0
    session['computer_wins'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
