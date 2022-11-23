# -- coding: utf-8 --
from flask import Flask, jsonify, request, render_template
import openai
import os

openai.api_type = "azure"
openai.api_base = "https://10b2bsi.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "22125b2f48e14c07a59e9c638005d33e"


def make_title(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003-pms",
        # prompt="summarize following conten" + prompt
        prompt="make the title with following content" + prompt,
        temperature=1,
        max_tokens=100,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)
    print("_______________________________________")
    print(response)
    # summary = response.messages[0].text.strip()
    title = response['choices'][0]['text']
    # summary = response.choices[0].message.content
    # print(text)
    return title


def summarize(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003-pms",
        # prompt="summarize following conten" + prompt
        prompt="summarize following content" + prompt,
        temperature=1,
        max_tokens=100,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)
    # summary = response.messages[0].text.strip()
    result = response['choices'][0]['text']
    # summary = response.choices[0].message.content
    # print(text)
    return result


app = Flask('__main__')
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/summary', methods=['GET'])
def summary():
    prompt = request.args.get('prompt')
    title = make_title(prompt)
    result = summarize(prompt)
    writer = request.args.get('writer')
    date = request.args.get('date')
    return render_template('summary.html',
                           writer=writer, date=date, summary=result, title=title)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
