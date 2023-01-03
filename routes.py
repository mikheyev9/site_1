from app import app
from flask import render_template

@app.route('/')
def main():
    return render_template('base.html')


@app.route('/tours/')
def tours():
    return render_template('tour.html')

@app.route('/departure/')
def departure():
    return render_template('departure.html')

@app.route('/index/')
def index():
    return render_template('index.html')
