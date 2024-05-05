from flask import Flask, render_template, redirect, url_for, request
import subprocess
import webbrowser
import os
from openpose6 import home  # Assuming home function is defined in openpose6.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/physio')
def physio():
    return render_template('physio.html')

@app.route('/acu')
def acu():
    return render_template('acu.html')

@app.route('/run_function')
def run_function():
    # Call the handle_home function when '/run_function' is requested
    return home()

@app.route('/run_server', methods=['POST'])
def run_server():
    # Change directory to the AR folder
    ar_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'AR'))
    os.chdir(ar_folder_path)

    # Run the Python server command
    subprocess.Popen(['python', '-m', 'http.server', '8000'])

    # Open the URL in the default web browser
    webbrowser.open('http://localhost:8000/acumaster.html')

    return redirect(url_for('acu'))

if __name__ == "__main__":
    app.run(debug=True)
