from flask import Flask, session, render_template, request
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Acts2:38'
boggle_game = Boggle()

def init_board():
  '''Creates a new board.'''
  session['board'] = boggle_game.make_board()

@app.before_first_request
def setup():
  '''Setup initial values for high_score and times_played.'''
  session['high_score'] = 0
  session['times_played'] = 0

@app.route('/')
def home():
  '''Render home page.'''
  return render_template('home.html')

@app.route('/board')
def board():
  '''Starts board and render board page.'''
  init_board()

  return render_template('board.html')

@app.route('/guess', methods=['POST'])
def guess():
  '''Accepts guess and runs it through Boggle.check_valid_word.'''
  req = request.get_json()
  guess = req['guess']

  res = boggle_game.check_valid_word(session['board'], guess)
  return res

@app.route('/endgame', methods=['POST'])
def endgame():
  '''Runs when game is complete to store new_score as high_score (if higher then already in session) and increases the times_played in session.'''
  req = request.get_json()
  new_score = req['score']

  if new_score > session['high_score']:
    session['high_score'] = new_score
  
  session['times_played'] += 1
  
  return 'ok', 200
