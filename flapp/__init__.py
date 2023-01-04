from flask import Flask, render_template, request,flash, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/', methods = ['GET', 'POST'])
def landing_page():
    stat = ''
    if request.method == 'POST':
        if request.form['Class'] == 'Mage':
           stat = 'int'
        elif request.form['Class'] == 'Fighter':
            stat = 'str'
        elif request.form['Class'] == 'Theif':
            stat = 'agl'
    return render_template('landing.html')


@app.route('/fighter', methods = ['GET', 'POST'])
def fihgting():
    return render_template('fight.html')

if __name__ == '__main__':
  app.debug = True
  app.run()
