from flask import render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
from app.forms import InputForm
import algo

TEST_FOLDER = "test"

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm()
    err = False
    if form.validate_on_submit():
        result = algo.search(form.folder.data, form.keyword.data, form.algo.data, TEST_FOLDER)
        return render_template('index.html', title='String Matcher - 13518030', form=form, result=result, keyword=form.keyword.data)
    return render_template('index.html', title='String Matcher - 13518030', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me")