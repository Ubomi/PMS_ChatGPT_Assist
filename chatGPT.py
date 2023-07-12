# -- coding: utf-8 --
from flask import Flask, jsonify, request, render_template
import openai
import os

# openai.api_type = "azure"
# openai.api_base = "https://10b2bsi.openai.azure.com/"
# openai.api_version = "2022-12-01"
# openai.api_key = "22125b2f48e14c07a59e9c638005d33e"
openai.api_key = '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'


def make_title(prompt):
    response = openai.Completion.create(
        # engine="text-davinci-003-pms",
        model="text-davinci-003",
        # prompt="summarize following conten" + prompt
        prompt="다음 내용으로 짧은 제목을 만들어줘. " + prompt,
        temperature=0,
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
        model="text-davinci-003",
        # engine="text-davinci-003-pms",
        # prompt="summarize following conten" + prompt
        prompt="summarize following content. " + prompt,
        temperature=0,
        max_tokens=2500,
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


def check(prompt, meeting, project):
    meeting = str(meeting)
    project = str(project)
    prompt = str("meeting: ") + meeting + str("Project: ") + \
        project + str("meeting: ")+prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        # engine="text-davinci-003-pms",
        # prompt="summarize following conten" + prompt
        prompt="""다음 내용에서 이슈 리스크만 추출해줘.
        Issue/Risk 컬럼에는 Issue 인지 Risk 인지 판단해줘.
        Conetents 에는 이슈 및 리스크 내용을 적어줘.
        (name, Issue or Risk, Contents, Due date) 컬럼으로 테이블을 만들어줘.""" + prompt,
        temperature=1,
        max_tokens=2500,
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


def testMaker(project, testTarget, testItem):
    project = str(project)
    testTarget = str(testTarget)
    testItem = str(testItem)
    prompt = str("project: ") + project + str("test target: ") + \
        testTarget + str("test Item: ") + testItem

    response = openai.Completion.create(
        model="text-davinci-003",
        # engine="text-davinci-003-pms",
        # prompt="summarize following conten" + prompt
        prompt="Make sub test Case with following master test cases. " + prompt,
        temperature=1,
        max_tokens=2500,
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
