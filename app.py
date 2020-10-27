# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:12:09 2020

@author: Niketan
"""

from mainfile import emotionproc
from flask import Flask, render_template,url_for,request
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home_temp.html') 


# @app.route('/')
# def func():
#     t=emotionproc('i love you')
#     return t

@app.route('/',methods=['POST'])
def mainfunc():
     text =request.form['u']
     text,w=emotionproc(text)
     d={}
     for a,b in zip(w.keys(),w.values()):
         d[a]=b
     d=str(d)
     return render_template('result.html',txt=text,txt2=d)

if __name__=='__main__':
    app.run(debug=True)
