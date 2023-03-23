from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    pattern = request.form['pattern']
    text = request.form['text']
    matches = re.findall(pattern, text)
    return render_template('result.html', pattern=pattern, text=text, matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
