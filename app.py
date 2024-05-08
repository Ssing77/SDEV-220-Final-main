#Name: Sahajpreet Singh, Nolan King, Cassarnda Corbin
#Project: SDEV220 Final Project - English Dictionary
from flask import Flask, render_template, request
import json
from difflib import get_close_matches

app = Flask(__name__)
# the app routing with flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])

#app.py brings all the code together from the python and html files,
#and runs it as a web application using Flask

#translate function
def translate():
    with open('dictionary_compact.json') as f:
        data = json.load(f)

    word = request.form['word'].lower()
#if the word is found in the dictionary
    if word in data:
        return render_template('result.html', word=word, definition=data[word])
    elif word.title() in data:
        return render_template('result.html', word=word, definition=data[word.title()])
    elif word.upper() in data:
        return render_template('result.html', word=word, definition=data[word.upper()])
    elif len(get_close_matches(word, data.keys())) > 0:
#if word is not found in the json dictionary file, it finds the closest match, and suggests it to the user,
#after which the user needs to input the suggestion, or a new word into the search bar.
        suggestion = get_close_matches(word, data.keys())[0]
        return render_template('suggestion.html', suggestion=suggestion)
#when the user enters a word or characters comepletely unrecognizable, the code returns an error,
#and tells the user to search another word.
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
