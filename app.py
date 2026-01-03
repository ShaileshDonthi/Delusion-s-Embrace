from flask import Flask, render_template, request, jsonify, session
from game_engine import GameEngine
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
engine = GameEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    session['game_state'] = GameEngine.get_initial_state()
    response = engine.process_step(session['game_state'])
    session.modified = True
    return jsonify(response)

@app.route('/choice', methods=['POST'])
def make_choice():
    data = request.json
    choice_index = data.get('choice_index')
    
    if 'game_state' not in session:
        return jsonify({"error": "No game session"}), 400
        
    state = session['game_state']
    response = engine.process_step(state, choice_index)
    session.modified = True
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
