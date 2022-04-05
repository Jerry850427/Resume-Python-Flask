# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:04:47 2021

@author: 高漢佑
"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("index.html")

@app.route('/home')
def test():
	return redirect(url_for('home'))

@app.route('/forward',methods=['POST'])
def inf():
    return redirect(url_for('m'))

@app.route('/experience')
def experience():
    return render_template("index2.html")

@app.route('/research')
def research():
    return render_template("index3.html")

@app.route('/education')
def education():
    return render_template("index4.html")

@app.route('/skills')
def skills():
    return render_template("index5.html")

@app.route('/publication')
def publication():
    return render_template("index6.html")

if __name__ == '__main__':
    app.run(debug=False)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0