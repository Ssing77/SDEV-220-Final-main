from flask import Flask, render_template, request
import json
from difflib import get_close_matches

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    with open('dictionary_compact.json') as f:
        data = json.load(f)

    word = request.form['word'].lower()

    if word in data:
        return render_template('result.html', word=word, definition=data[word])
    elif word.title() in data:
        return render_template('result.html', word=word, definition=data[word.title()])
    elif word.upper() in data:
        return render_template('result.html', word=word, definition=data[word.upper()])
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = get_close_matches(word, data.keys())[0]
        return render_template('suggestion.html', suggestion=suggestion)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
