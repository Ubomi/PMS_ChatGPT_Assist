# -- coding: utf-8 --
from flask import Flask, jsonify, request, render_template
import openai
import os
import chatGPT


app = Flask('__main__')
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/summary_home', methods=['GET'])
def summary_home():
    return render_template('summary_home.html')


@app.route('/summary_result', methods=['GET'])
def summary_result():
    prompt = request.args.get('prompt')
    title = chatGPT.make_title(prompt)
    result = chatGPT.summarize(prompt)
    writer = request.args.get('writer')
    date = request.args.get('date')
    return render_template('summary_result.html',
                           writer=writer, date=date, summary=result, title=title)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
