from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/more/sidebar-left')
def sidebarleft():
    return render_template('sidebar-left.html')


@app.route('/more/sidebar-right')
def sidebarright():
    return render_template('sidebar-right.html')

