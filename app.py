from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Card setup
suits = ['A', 'B', 'C', 'D']
cards = {suit: list(range(1, 14)) for suit in suits}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/api/cards')
def get_cards():
    deck = {suit: random.sample(cards[suit], len(cards[suit])) for suit in suits}
    hidden_cards = random.sample(range(1, 14), 5)  # Random hidden cards
    return jsonify(deck=deck, hidden_cards=hidden_cards)

if __name__ == '__main__':
    app.run(debug=True)
