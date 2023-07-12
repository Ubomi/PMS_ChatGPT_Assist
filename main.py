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


@app.route('/issue_home', methods=['GET'])
def issue_home():
    return render_template('issue_home.html')


@app.route('/issue_result', methods=['GET', 'POST'])
def issue_result():
    prompt = request.args.get('prompt')
    meeting = request.args.get('meeting')
    project = request.args.get('project')
    title = chatGPT.make_title(prompt)
    IRlist = chatGPT.check(prompt, meeting, project)
    writer = request.args.get('writer')
    date = request.args.get('date')
    return render_template('issue_result.html',
                           writer=writer, date=date, IRlist=IRlist, title=title)


@app.route('/testCase_home', methods=['GET'])
def testCase_home():
    return render_template('testCase_home.html')


@app.route('/testCase_result', methods=['GET', 'POST'])
def testCase_result():
    testTarget = request.args.get('testTarget')
    testItem = request.args.get('testItem')
    project = request.args.get('project')
    writer = request.args.get('writer')
    date = request.args.get('date')
    title = chatGPT.make_title("test Item :"+testItem)
    subTestCase = chatGPT.testMaker(project, testTarget, testItem)
    return render_template('testCase_result.html',
                           writer=writer, date=date, subTestCase=subTestCase, title=title)


@app.route('/LR_home', methods=['GET'])
def LR_home():
    return render_template('LR_home.html')


@app.route('/LR_result', methods=['GET', 'POST'])
def LR_result():
    transaction = request.args.get('transaction')
    url = str(request.args.get('url'))
    header = str(request.args.get('header'))
    body = str(request.args.get('body'))
    passFail = str(request.args.get('passFail'))

    prompt = '아래의 데이터로 LoadRunner로 부하를 발생시키는 Script를 작성해줘. transaction 이름: ' + transaction
    prompt = prompt + ", 테스트 대상 URL :" + url
    prompt = prompt + ", web_add_header로 다음의 헤더 정보를 추가해줘. " + header
    prompt = prompt + ", web_custom_request로 다음의 Body 정보를 추가해줘. " + body
    prompt = prompt + ", Transaction 성공 여부는 web_reg_find 명령어를 사용해줘. Transaction 종료는 LR_AUTO로 처리해줘."

    return render_template('LR_result.html', prompt=prompt)


@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Im Bommi"
            },
            {
                "role": "user",
                "content": f"{user_text}"
            }
        ]
    )
    return str(response['choices'][0]['message']['content'])


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
