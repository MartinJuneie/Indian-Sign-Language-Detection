from flask import Flask, render_template
import subprocess
import os
import signal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_letter')
def run_letter():
    subprocess.run(['python', 'letters.py'])
    return 'Letter.py is running'

@app.route('/run_words')
def run_words():
    subprocess.run(['python', 'words.py'])
    return 'Words.py is running'

@app.route('/clear_program')
def clear_program():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Program terminated'

if __name__ == '__main__':
    app.run()
