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
        prompt="make the title with following content. " + prompt,
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
        prompt="summarize following content. " + prompt,
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
