#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
  return json.dumps({'Event': 'Hackathon-2022',
                           'Message': 'Welcome to CIO Hackathon!'})

@app.route('/input', methods=['POST'])
def process_json():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)
            response = json
            return response
        else:
            return 'Content-Type not supported!'

app.run()



