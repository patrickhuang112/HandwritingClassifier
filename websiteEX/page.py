import os
from flask import Flask, render_template, request


app=Flask(__name__)
@app.route('/')
def home():
        return render_template('home.html')

@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        if request.form['submit'] == 'run':
            os.system("rm templates/output.html; touch templates/output.html; python hello.py >> templates/output.html")
        return render_template('output.html')
    else:
        return render_template('run.html')

if __name__ == '__main__':
    app.run(debug=True)
