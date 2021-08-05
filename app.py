from flask import Flask, session, render_template, request
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Acts2:38'
boggle_game = Boggle()

def init_board():
  session['board'] = boggle_game.make_board()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/board')
def board():
  init_board()

  return render_template('board.html')

@app.route('/guess', methods=['POST'])
def guess():
  req = request.get_json()
  guess = req['guess']

  res = boggle_game.check_valid_word(session['board'], guess)
  return res